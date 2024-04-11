import numpy as np


def sum_arrays(arr1, arr2):
    # Check if the arrays have compatible shapes
    assert len(arr1.shape) == 1 and len(arr2.shape) == 2, "Arrays must be of shape (n,) and (m,n)"


    # Compute the sum
    result = np.sum(np.multiply(arr1.reshape(-1, 1), arr2))


    return result


# Define input arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4], [5], [6]])


# Call function with assertions to verify output
assert sum_arrays(arr1, arr2) == 32, f"Expected sum_arrays({arr1}, {arr2}) to return 32 but got {sum_arrays(arr1, arr2)}"


print("All tests passed!")