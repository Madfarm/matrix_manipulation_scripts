from sympy import symbols, Eq, solve

# Declare the variable
x = symbols('x')

# Declare the equation
equation = Eq(x**2 + 5*x - 3, 0)

# Solve the equation
solution = solve(equation, x)

print(solution)