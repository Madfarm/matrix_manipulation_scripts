import numpy as np


# Define the matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])


matrix2 = np.array([[7, 8],
                    [9, -10],
                    [11, 12]])


# Multiply the matrices
result = np.dot(matrix1, matrix2)


# Calculate the cumulative sum of the resulting matrix
cumulative_sum = np.cumsum(result)


# Print the result
print(cumulative_sum)