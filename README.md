# Flexible Production Schedule Optimization with Maintenance Constraints

## Problem Description

You are managing a production line with multiple machines, each capable of producing different products. Each machine has a specific maintenance schedule that requires it to be idle for a certain number of hours every week. The goal is to optimize the production schedule to maximize the total profit while respecting these maintenance constraints.

## Problem Formulation

- **Variables:**
  - `x_{p,m,t}`: Amount of product \( p \) produced by machine \( m \) during time slot \( t \).

- **Parameters:**
  - `p_m`: Profit per unit of product \( p \) produced by machine \( m \).
  - `h_m`: Hours of operation per time slot for machine \( m \).
  - `d_{p,m}`: Production rate of product \( p \) by machine \( m \) (units per hour).
  - `M_m`: Maximum hours machine \( m \) can operate per week.
  - `R_m`: Required maintenance hours for machine \( m \) per week.
  - `T`: Total number of time slots in a week.

- **Objective:**
  - Maximize the total profit from all products produced.

- **Constraints:**
  - The total production time for each machine must not exceed its available hours after accounting for maintenance.
  - Production levels must be non-negative.

## Example Data

- **Machines:** Machine 1, Machine 2
- **Products:** Product A, Product B
- **Time slots:** 10 hours each

| Machine | Product | Profit (per unit) | Production Rate (units/hour) |
|---------|---------|--------------------|-------------------------------|
| 1       | A       | 20                 | 5                             |
| 1       | B       | 30                 | 3                             |
| 2       | A       | 15                 | 4                             |
| 2       | B       | 25                 | 6                             |

**Maintenance constraints:**
- Machine 1: Maximum 50 hours per week, requires 10 hours of maintenance
- Machine 2: Maximum 60 hours per week, requires 15 hours of maintenance

## Model Description

This optimization problem involves complex scheduling and capacity planning. It aims to maximize profit by optimizing the production schedule of different products on multiple machines while respecting machine-specific operational and maintenance constraints.

## How to Use

1. Define the parameters for each machine and product, including profits, production rates, and maintenance requirements.
2. Set up the optimization model using these parameters.
3. Solve the model to determine the optimal production schedule that maximizes profit.
4. Review the results to see the amount of each product produced by each machine in each time slot, along with the total profit.

