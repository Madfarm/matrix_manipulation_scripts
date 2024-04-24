import numpy as np
from fractions import Fraction


def inverse_matrix(matrix):
    # Check if the input is a 2D numpy array
    assert len(matrix.shape) == 2, "Input must be a 2D numpy array"


    # Check if the matrix is square
    assert matrix.shape[0] == matrix.shape[1], "Input matrix must be square"


    # Calculate the determinant of the matrix
    det = np.linalg.det(matrix.astype(float))


    # Check if the matrix is singular
    assert det != 0, "Matrix is singular and does not have an inverse"


    # Calculate the inverse of the matrix
    inv = np.linalg.inv(matrix.astype(float))


    # Convert the elements of the inverse to fractions
    inv = np.array([[Fraction(x).limit_denominator() for x in row] for row in inv])


    # Check if the inverse is a 2D numpy array with the same shape as the input
    assert isinstance(inv, np.ndarray) and len(inv.shape) == 2, "Output must be a 2D numpy array"
    assert inv.shape == matrix.shape, "Output shape must match input shape"


    return inv


# Test the function
matrix = np.array([[Fraction(1, 2), Fraction(1, 3)],
                   [Fraction(1, 4), Fraction(1, 5)]])
