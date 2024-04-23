import numpy as np
from fractions import Fraction


def fractional_matrix_operations(matrix_a, matrix_b, operation):
    assert operation in ["add", "subtract", "multiply", "divide"], "Invalid operation"


    if operation == "add":
        result = np.add(matrix_a, matrix_b)
    elif operation == "subtract":
        result = np.subtract(matrix_a, matrix_b)
    elif operation == "multiply":
        result = np.multiply(matrix_a, matrix_b)
    elif operation == "divide":
        result = np.divide(matrix_a, matrix_b)


    # Ensure the resulting matrix contains fractions
    result = np.vectorize(Fraction)(result)


    return result


matrix_a = np.array([[Fraction(1, 2), Fraction(1, 3)], [Fraction(1, 4), Fraction(1, 5)]])
matrix_b = np.array([[Fraction(1, 4), Fraction(1, 5)], [Fraction(1, 6), Fraction(1, 7)]])


# Addition operation
result_addition = fractional_matrix_operations(matrix_a, matrix_b, "add")


# Assertion to verify the contents of the final array
assert np.array_equal(result_addition, np.array([[Fraction(3, 4), Fraction(4, 15)], [Fraction(5, 12), Fraction(12, 35)]])), "Resulting array is not as expected"