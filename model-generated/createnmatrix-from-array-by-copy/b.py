import numpy as np


def array_to_matrix(arr):
    assert len(arr) > 0, "Input array is empty"
    assert all(isinstance(x, (int, float)) for x in arr), "Input array contains non-numeric elements"


    if 0 in arr:
        return None
    else:
        return np.array([arr] * len(arr))


# Test the function
arr = [5, 8, 12, 99]
matrix = array_to_matrix(arr)


assert matrix.shape == (len(arr), len(arr)), "Matrix shape is incorrect"
assert np.all(matrix == arr), "Matrix rows are not copies of the original array"

