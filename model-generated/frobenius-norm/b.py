import numpy as np


def frobenius_norm(matrix):
    assert isinstance(matrix, list), "Input must be a list"
    assert all(isinstance(row, list) for row in matrix), "Input must be a 2D list"
    assert all(all(isinstance(x, (int, float)) for x in row) for row in matrix), "All elements in the input list must be numbers"


    matrix = np.array(matrix)
    norm = np.linalg.norm(matrix)


    assert isinstance(norm, float), "Frobenius norm must be a float"


    return norm


# Test the function
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]