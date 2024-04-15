import numpy as np


def transform_arrays(arr1, arr2):
    # Remove non-numerical values
    arr1 = [x for x in arr1 if isinstance(x, (int, float))]
    arr2 = [x for x in arr2 if isinstance(x, (int, float))]


    # Truncate floats to integers
    arr1 = [int(x) for x in arr1]
    arr2 = [int(x) for x in arr2]


    # Add zeros to the shorter array
    len_diff = len(arr1) - len(arr2)
    if len_diff > 0:
        arr2 += [0] * len_diff
    elif len_diff < 0:
        arr1 += [0] * abs(len_diff)


    return arr1, arr2


def calculate_square_difference(arr1, arr2):
    # Convert lists to numpy arrays
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)


    # Calculate element-wise square of difference
    diff = arr1 - arr2
    squared_diff = diff ** 2


    return squared_diff


# Test the program
arr1 = [.235, np.nan, "Applesauce", 5, 15, 2, 7, "wow", 8.21, 3.3333333333, None]
arr2 = [np.nan, np.nan, 5, 5, "shoe", 9.99, 12, 3.617]


arr1, arr2 = transform_arrays(arr1, arr2)
squared_diff = calculate_square_difference(arr1, arr2)


print(squared_diff)