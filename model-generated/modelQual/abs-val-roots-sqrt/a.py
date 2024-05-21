import sympy as sp

# Define the variable
a = sp.symbols('a')

# Define the equation
equation = sp.Abs(sp.sqrt(12*a + 25) / a) - sp.sqrt(61) / 3

# Solve the equation
solution = sp.solve(equation, a)[0]

# Print the solution
print(solution)