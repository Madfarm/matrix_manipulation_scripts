import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix2 = np.array([[7, 8],
                    [9, -10],
                    [11, 12]])

# Perform matrix multiplication using numpy.dot()
result_matrix = np.dot(matrix1, matrix2)

# Alternatively, you can use the @ operator
# result_matrix = matrix1 @ matrix2

cum = np.cumsum(result_matrix)

# Display the result
print(cum)