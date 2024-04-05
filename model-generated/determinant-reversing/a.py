from scipy.linalg import det
import numpy as np


# Input matrix
matrix = np.array([[6, 7, 8], [3, 4, 5], [0, 1, 2]])


# Calculate determinant
det_value = det(matrix)


# Add determinant to each value in the matrix
matrix += det_value


# Reverse the rows in the matrix
reversed_matrix = matrix[::-1, :]


# Print the resulting matrix
print(reversed_matrix)