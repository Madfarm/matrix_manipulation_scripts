import numpy as np

# Generate a 8x8 matrix with random integers from 1 to 100
matrix_A = np.random.randint(1, 101, size=(8, 8))

# Compute the determinant of the matrix
determinant_A = np.linalg.det(matrix_A)

# If the determinant is non-zero, calculate the inverse of the matrix
if determinant_A != 0:
    print("Matrix A is invertible")
    inverse_A = np.linalg.inv(matrix_A)
    print(inverse_A)
else:
    print("Matrix A is singular")
