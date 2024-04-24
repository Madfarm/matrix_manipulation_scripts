import numpy as np
from decimal import Decimal


def create_matrix():
    return np.zeros((3, 3))


def input_number(matrix, row, column, value):
    matrix[row, column] = value


def add_matrices(matrix1, matrix2):
    assert matrix1.shape == matrix2.shape, "Matrices must be the same size"
    return matrix1 + matrix2


def scalar_multiply(matrix, scalar):
    return matrix * scalar


# Create matrices
matrix = create_matrix()
input_number(matrix, 0, 0, Decimal('3.14'))
input_number(matrix, 1, 2, Decimal('5.00'))


matrix2 = create_matrix()
input_number(matrix2, 0, 0, Decimal('2.71'))
input_number(matrix2, 1, 2, Decimal('1.25'))


# Add matrices
result = add_matrices(matrix, matrix2)
assert np.allclose(result, np.array([[5.85, 0.0, 0.0], [0.0, 0.0, 6.25], [0.0, 0.0, 0.0]])), "Matrix addition failed"


# Multiply by scalar
result = scalar_multiply(matrix, Decimal('2'))
assert np.allclose(result, np.array([[6.28, 0.0, 0.0], [0.0, 0.0, 10.00], [0.0, 0.0, 0.0]])), "Scalar multiplication failed"