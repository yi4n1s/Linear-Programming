# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 03:37:32 2023

@author: Constantinos
"""

# Import the necessary libraries
from pulp import *


# Define the transportation problem
# Supply and demand values
supply = [200, 300, 500]
demand = [100, 200, 300, 400]

# Cost matrix
costs = [[2, 4, 5, 3],
         [3, 6, 7, 4],
         [4, 8, 9, 5]]

# Define the problem as a minimization problem
prob = LpProblem("Transportation Problem", LpMinimize)

# Define the decision variables
rows = range(len(supply))
cols = range(len(demand))
vars = LpVariable.dicts("Route", (rows, cols), lowBound=0, cat='Integer')

# Define the objective function
prob += lpSum([vars[i][j]*costs[i][j] for i in rows for j in cols])

# Define the supply constraints
for i in rows:
    prob += lpSum([vars[i][j] for j in cols]) <= supply[i]

# Define the demand constraints
for j in cols:
    prob += lpSum([vars[i][j] for i in rows]) == demand[j]

# Solve the problem
prob.solve()

# Print the optimal solution
print("Optimal Solution:")
total_cost = 0
for i in rows:
    for j in cols:
        if vars[i][j].value() > 0:
            print("Shipping %d units from factory %d to warehouse %d" % (vars[i][j].value(), i+1, j+1))
            total_cost += vars[i][j].value() * costs[i][j]
print("Total cost: $%s" % total_cost)
