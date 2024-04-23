import numpy as np
from fractions import Fraction


def fractional_matrix_operations(matrix_a, matrix_b, operation):
    # Perform the specified operation on matrix_a and matrix_b element-wise
    if operation == "add":
        result = matrix_a + matrix_b
    elif operation == "subtract":
        result = matrix_a - matrix_b
    elif operation == "multiply":
        result = matrix_a * matrix_b
    elif operation == "divide":
        result = matrix_a / matrix_b
    else:
        raise ValueError("Invalid operation. Please choose from: add, subtract, multiply, divide")


    # Ensure that the result is a two-dimensional numpy array with elements represented as fractions
    result = np.vectorize(Fraction)(result)


    return result


matrix_a = np.array([[Fraction(1, 2), Fraction(1, 3)], [Fraction(1, 4), Fraction(1, 5)]])
matrix_b = np.array([[Fraction(1, 4), Fraction(1, 5)], [Fraction(1, 6), Fraction(1, 7)]])


# Addition operation
result_addition = fractional_matrix_operations(matrix_a, matrix_b, "add")
print(result_addition)