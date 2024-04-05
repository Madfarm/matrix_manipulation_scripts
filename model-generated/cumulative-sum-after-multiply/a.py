import numpy as np


# Define two matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])


matrix2 = np.array([[7, 8],
                    [9, -10],
                    [11, 12]])


# Multiply the matrices
result = np.dot(matrix1, matrix2)


# Calculate the cumulative sum
cumulative_sum = np.cumsum(result)


# Print the result
print("Resultant Matrix:\n", result)
print("\nCumulative Sum:\n", cumulative_sum)