import sympy as sp

# Define the variable
a = sp.symbols('a')

# Define the quadratic equation
equation = a * sp.symbols('x')**2 + 5*sp.symbols('x') - 3

# Solve the equation using the quadratic formula
solutions = sp.solve(equation, sp.symbols('x'))

# Print the solutions
print(solutions)