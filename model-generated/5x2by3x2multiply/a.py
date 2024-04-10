# 5x3 matrix
matrix_5x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]


# 3x2 matrix
matrix_3x2 = [
    [16, 17],
    [18, 19],
    [20, 21]
]


# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])


    # Check if the matrices can be multiplied
    if cols_matrix1 != rows_matrix2:
        return "Matrices cannot be multiplied"


    # Create a result matrix with zeros
    result = [[0 for row in range(cols_matrix2)] for col in range(rows_matrix1)]


    # Multiply the matrices
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):  # or for k in range(rows_matrix2)
                result[i][j] += matrix1[i][k] * matrix2[k][j]


    return result


# Multiply the matrices
result = multiply_matrices(matrix_5x3, matrix_3x2)


# Print the result
for row in result:
    print(row)