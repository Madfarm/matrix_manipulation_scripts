from fractions import Fraction
import numpy as np

def multiply_matrices(matrix1, matrix2):
    # Validate the input matrices
    assert isinstance(matrix1, list) and isinstance(matrix2, list), "Input matrices must be lists of lists"
    assert all(isinstance(row, list) for row in matrix1) and all(isinstance(row, list) for row in matrix2), "Input matrices must be lists of lists"
    assert all(all(isinstance(element, (int, float)) for element in row) for row in matrix1) and all(all(isinstance(element, (int, float)) for element in row) for row in matrix2), "All elements in the input matrices must be numbers"


    # Convert the input matrices to NumPy arrays
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)


    # Check if the matrices can be multiplied
    assert matrix1.shape[1] == matrix2.shape[0], "The number of columns in the first matrix must be equal to the number of rows in the second matrix"


    # Multiply the matrices
    result = np.dot(matrix1, matrix2)


    # Convert the result to a list of lists with Fraction elements
    result = [[Fraction(element) for element in row] for row in result]


    return result


# Test the function
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 0], [1, 3]]
result = multiply_matrices(matrix1, matrix2)
assert result == [[Fraction(4, 1), Fraction(6, 1)], [Fraction(10, 1), Fraction(12, 1)]]