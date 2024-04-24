import numpy as np
from fractions import Fraction


def transpose_fraction_matrix(matrix):
    # Check if the input is a numpy array
    assert isinstance(matrix, np.ndarray), "Input must be a numpy array"


    # Check if the numpy array is two-dimensional
    assert len(matrix.shape) == 2, "Input must be a two-dimensional numpy array"


    # Calculate the transpose of the matrix
    transposed_matrix = matrix.T


    # Check if all elements in the transposed matrix are fractions
    assert all(isinstance(element, Fraction) for row in transposed_matrix for element in row), "All elements in the transposed matrix must be fractions"


    return transposed_matrix


# Create a sample matrix with fractional elements
matrix = np.array([[Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)],
                   [Fraction(1, 5), Fraction(1, 6), Fraction(1, 7)]])


# Calculate and print the transpose of the matrix
transposed_matrix = transpose_fraction_matrix(matrix)
