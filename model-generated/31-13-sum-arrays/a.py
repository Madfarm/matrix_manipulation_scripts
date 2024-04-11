import numpy as np


def sum_arrays(arr1, arr2):
    # Check if the arrays have compatible shapes
    assert len(arr1.shape) == 1 and len(arr2.shape) == 2, "Array 1 must be a 1D array and Array 2 must be a 2D array"
    assert arr1.size == arr2.shape[0], f"Number of elements in arr1 ({arr1.size}) is not equal to number of rows in arr2 ({arr2.shape[0]})"


    result = []
    for i in range(len(arr1)):
        temp_sum = arr1[i]
        for j in range(len(arr2[:,0])):
            temp_sum += arr2[j,:][i]
        result.append(temp_sum)


    return np.array(result)


# Test the function with example inputs:
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4], [5], [6]])


output = sum_arrays(arr1, arr2)
print(output)