% minimize x + 2y + z subject to the constraints:
% x + y + z >= 10
% x + 2y + 3z <= 25
% x, y, z >= 0

f = [1; 2; 1]; % objective function coefficients
A = [-1 -1 -1; 1 2 3]; % matrix of coefficients for the constraints
b = [-10; 25]; % right-hand side of the constraints
lb = [0; 0; 0]; % lower bounds for the variables

[x, fval] = glpk(f, A, b, lb) % solve the LP using GLPK solver
