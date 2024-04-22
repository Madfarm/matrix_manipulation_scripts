from sympy import symbols, Eq, solve, simplify


def solve_equation(equation):
    x = symbols('x')
    equation = equation.replace('^', '**')  # Convert ^ to ** for SymPy
    equation = Eq(eval(equation.replace('=', '-(') + ')'), 0)  # Convert = to -() for SymPy
    simplified = simplify(equation)
    solutions = solve(simplified, x)


    return simplified, solutions


# Test the function
equation = "x^2 - 4 = 0"
simplified, solutions = solve_equation(equation)


assert str(simplified) == 'Eq(x**2, 4)'
assert solutions == [-2, 2]