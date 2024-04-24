import numpy as np
from fractions import Fraction


def transpose_matrix(matrix):
    # Check if the input is a 2D numpy array
    assert len(matrix.shape) == 2, "Input must be a 2D numpy array"


    # Calculate the transpose of the matrix
    transposed_matrix = matrix.T


    # Check if the output is a 2D numpy array
    assert len(transposed_matrix.shape) == 2, "Output must be a 2D numpy array"


    return transposed_matrix


# Create a matrix with fractional elements
matrix = np.array([[Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)],
                   [Fraction(1, 5), Fraction(1, 6), Fraction(1, 7)]])


# Calculate the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)


# Print the original and transposed matrices
print("Original Matrix:")
print(matrix)
print("\nTransposed Matrix:")
print(transposed_matrix)