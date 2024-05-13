import numpy as np

def matrix_power(matrix, power):
    assert isinstance(matrix, np.ndarray), "Input must be a numpy array"
    assert len(matrix.shape) == 2, "Input must be a 2D array"
    assert matrix.shape[0] == matrix.shape[1], "Input must be a square matrix"
    assert isinstance(power, int) and power >= 0, "Power must be a non-negative integer"

    result = np.eye(matrix.shape[0])
    for _ in range(power):
        result = np.dot(result, matrix)

    return result

matrix = np.array([[1, 2], [3, 4]])
power = 3
print(matrix_power(matrix, power))