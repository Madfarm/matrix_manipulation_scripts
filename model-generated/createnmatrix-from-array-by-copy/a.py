import numpy as np


def check_zeros_and_create_matrix(arr):
    assert isinstance(arr, list), "Input must be a list"
    assert len(arr) > 0, "List must not be empty"


    if 0 in arr:
        return "There are zeros in the array"
    else:
        return np.array([arr]*len(arr))


# Test the function
print(check_zeros_and_create_matrix([5,8,12,99]))


# Test assertions
try:
    print(check_zeros_and_create_matrix(5))
except AssertionError as e:
    print(e)


try:
    print(check_zeros_and_create_matrix([]))
except AssertionError as e:
    print(e)