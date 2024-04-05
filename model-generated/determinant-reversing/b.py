import scipy.linalg as la
import numpy as np


def add_det(num, x):
    return num + x

# Input matrix
matrix = np.array([[6, 7, 8], [3, 4, 5], [0, 1, 2]])


# Calculate determinant
det = la.det(matrix)

# Add determinant to each value in the matrix
det_addition = np.vectorize(add_det)
result_matrix = det_addition(matrix, det)


# Reverse the rows in the resulting matrix
result_matrix = np.flipud(result_matrix)


# Output the resulting matrix
print(result_matrix)