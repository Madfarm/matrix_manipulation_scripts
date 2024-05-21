import sympy as sp

# Define the variable
a = sp.symbols('a')

# Define the equation
equation = sp.sqrt(12*a + 25) / a - sp.sqrt(61) / 3

# Solve the equation
solutions = sp.solve(equation, a)

# Print the solutions
print(solutions)