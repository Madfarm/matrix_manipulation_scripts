import numpy as np
from fractions import Fraction

def matrix_inverse(matrix):
    # Check if the input is a list of lists
    assert isinstance(matrix, list) and all(isinstance(row, list) for row in matrix), "Input must be a list of lists"
    
    # Check if the matrix is square
    assert len(matrix) == len(matrix[0]), "Matrix must be square"
    
    # Convert the matrix to a numpy array
    matrix = np.array(matrix)
    
    # Check if the matrix is invertible
    assert np.linalg.det(matrix) != 0, "Matrix must be invertible"
    
    # Calculate the inverse of the matrix
    inverse = np.linalg.inv(matrix)
    
    # Represent each element as a fraction
    inverse = [[Fraction(x).limit_denominator() for x in row] for row in inverse]
    
    return inverse

# Test the function
matrix = [[1, 2], [3, 4]]
assert matrix_inverse(matrix) == [[Fraction(-2, 1), Fraction(1, 1)], [Fraction(3, 2), Fraction(-1, 2)]]