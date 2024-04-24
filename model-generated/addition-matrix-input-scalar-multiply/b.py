from decimal import Decimal
import numpy as np


def create_matrix():
    return np.zeros((3, 3), dtype=object)


def input_number(matrix, row, col, value):
    matrix[row, col] = value


def add_matrices(matrix1, matrix2):
    assert matrix1.shape == matrix2.shape, "Matrices are not the same size"
    result = create_matrix()
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            result[i, j] = matrix1[i, j] + matrix2[i, j]
    return result


def scalar_multiply(matrix, scalar):
    result = create_matrix()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[i, j] = matrix[i, j] * scalar
    return result


# Test the program
matrix = create_matrix()
input_number(matrix, 0, 0, Decimal('3.14'))
input_number(matrix, 1, 2, Decimal('5.00'))


matrix2 = create_matrix()
input_number(matrix2, 0, 0, Decimal('2.71'))
input_number(matrix2, 1, 2, Decimal('1.25'))


added_matrix = add_matrices(matrix, matrix2)
assert added_matrix[0, 0] == Decimal('5.85')
assert added_matrix[1, 2] == Decimal('6.25')


scaled_matrix = scalar_multiply(matrix, Decimal('2'))
assert scaled_matrix[0, 0] == Decimal('6.28')
assert scaled_matrix[1, 2] == Decimal('10.00')