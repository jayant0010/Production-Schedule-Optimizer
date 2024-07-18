from pyomo.environ import *

# Create a model
model = ConcreteModel()

# Define sets for machines, products, and time slots
model.Machines = Set(initialize=['Machine1', 'Machine2'])
model.Products = Set(initialize=['ProductA', 'ProductB'])
model.TimeSlots = RangeSet(1, 10)  # 10 time slots (hours)

# Parameters for profits, production rates, max operational hours, and maintenance hours
model.Profits = Param(model.Machines, model.Products, initialize={
    ('Machine1', 'ProductA'): 20, ('Machine1', 'ProductB'): 30,
    ('Machine2', 'ProductA'): 15, ('Machine2', 'ProductB'): 25
})
model.Rates = Param(model.Machines, model.Products, initialize={
    ('Machine1', 'ProductA'): 5, ('Machine1', 'ProductB'): 3,
    ('Machine2', 'ProductA'): 4, ('Machine2', 'ProductB'): 6
})
model.MaxHours = Param(model.Machines, initialize={'Machine1': 50, 'Machine2': 60})
model.MaintenanceHours = Param(model.Machines, initialize={'Machine1': 10, 'Machine2': 15})

# Decision variable for the amount of each product produced by each machine in each time slot
model.x = Var(model.Products, model.Machines, model.TimeSlots, domain=NonNegativeReals)

# Objective function: Maximize total profit from all products produced
def objective_rule(model):
    return sum(model.Profits[m, p] * model.x[p, m, t] for p in model.Products for m in model.Machines for t in model.TimeSlots)
model.obj = Objective(rule=objective_rule, sense=maximize)

# Constraint: Total production time for each machine must not exceed available hours after maintenance
def time_constraint_rule(model, m):
    return sum(model.x[p, m, t] / model.Rates[m, p] for p in model.Products for t in model.TimeSlots) <= (model.MaxHours[m] - model.MaintenanceHours[m])
model.time_constraint = Constraint(model.Machines, rule=time_constraint_rule)

# Solver: Using GLPK (GNU Linear Programming Kit) to solve the model
solver = SolverFactory('glpk')
results = solver.solve(model, tee=True)

# Display the optimal production schedule and total profit
print("Optimal Production Schedule:")
for m in model.Machines:
    for p in model.Products:
        for t in model.TimeSlots:
            if model.x[p, m, t].value > 0:
                print(f"{p} produced by {m} in time slot {t}: {model.x[p, m, t].value:.2f} units")

print(f"Total Profit: {model.obj():.2f}")