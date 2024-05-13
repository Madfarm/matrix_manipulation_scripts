import numpy as np

def matrix_power(matrix, power):
    assert isinstance(power, int), "Power must be an integer"
    assert power >= 0, "Power must be a non-negative integer"
    assert len(matrix.shape) == 2, "Input must be a 2D matrix"
    assert matrix.shape[0] == matrix.shape[1], "Input matrix must be square"

    result = np.eye(matrix.shape[0])
    for _ in range(power):
        result = np.dot(result, matrix)

    return result

matrix = np.array([[1, 2], [3, 4]])
power = 3
assert np.array_equal(matrix_power(matrix, power), [[37, 54], [81, 118]]), "Resulting product is incorrect"