import numpy as np


def transform_arrays(arr1, arr2):
    # Remove non-numerical values from both arrays
    arr1 = [x for x in arr1 if isinstance(x, (int, float))]
    arr2 = [x for x in arr2 if isinstance(x, (int, float))]


    assert all(isinstance(x, (int, float)) for x in arr1)
    assert all(isinstance(x, (int, float)) for x in arr2)


    # Truncate floats to integers
    arr1 = [int(x) for x in arr1 if x is not np.nan]
    arr2 = [int(x) for x in arr2 if x is not np.nan]


    assert all(isinstance(x, int) for x in arr1)
    assert all(isinstance(x, int) for x in arr2)


    # Add 0s to the shorter array until they are both the same length
    max_len = max(len(arr1), len(arr2))
    arr1 += [0] * (max_len - len(arr1))
    arr2 += [0] * (max_len - len(arr2))


    assert len(arr1) == len(arr2)


    # Convert arrays to numpy arrays
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)


    assert isinstance(arr1, np.ndarray)
    assert isinstance(arr2, np.ndarray)


    # Calculate the element-wise square of the difference between them
    diff = (arr1 - arr2) ** 2


    return diff


# Test the function
arr1 = [.235, np.nan, "Applesauce", 5, 15, 2, 7, "wow", 8.21, 3.3333333333, None]
arr2 = [np.nan, np.nan, 5, 5, "shoe", 9.99, 12, 3.617]


print(transform_arrays(arr1, arr2))