import sympy as sp


def solve_equation(equation):
    # Define the variable(s) in the equation
    x = sp.symbols('x')


    # Parse the equation and solve it
    equation = sp.sympify(equation)
    solutions = sp.solve(equation, x)


    # If there are no solutions, return a message
    if len(solutions) == 0:
        return "No solutions found."


    # Otherwise, simplify the solutions and return them
    solutions = [sp.simplify(solution) for solution in solutions]
    return solutions


# Test the function
assert solve_equation("x^2 - 4 = 0") == [-2, 2], "Expected solutions [-2, 2] but got {}".format(solve_equation("x^2 - 4 = 0"))
print("Test passed. The solutions to the equation 'x^2 - 4 = 0' are: ", solve_equation("x^2 - 4 = 0"))