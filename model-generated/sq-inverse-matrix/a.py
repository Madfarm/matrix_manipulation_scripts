def inverse_matrix(matrix):
    assert len(matrix) == len(matrix[0]), "Input is not a square matrix"
    for row in matrix:
        for elem in row:
            assert isinstance(elem, (int, float)), "Matrix elements must be integers or floats"


    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and does not have an inverse")


    adjugate = [[(-1)**(i+j)*determinant(sub_matrix(matrix, i, j)) for j in range(len(matrix))] for i in range(len(matrix))]
    adjugate = transpose(adjugate)


    inv_matrix = [[Fraction(adjugate[i][j], det) for j in range(len(matrix))] for i in range(len(matrix))]


    return inv_matrix


def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            sub_mat = sub_matrix(matrix, 0, i)
            det += (-1)**i * matrix[0][i] * determinant(sub_mat)
        return det


def sub_matrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]


def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


from fractions import Fraction


# Demonstration
matrix = [[1, 2], [3, 4]]
print(inverse_matrix(matrix))