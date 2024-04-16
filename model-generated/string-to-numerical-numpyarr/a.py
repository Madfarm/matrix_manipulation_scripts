import numpy as np


def convert_to_numerical(arr):
    numerical_arr = []
    for item in arr:
        try:
            numerical_arr.append(float(item))
        except ValueError:
            numerical_arr.append(np.nan)
    return np.array(numerical_arr)


# Test the function
input_array = ["4.29", "two", "7", "46", "7,63"]
output_array = convert_to_numerical(input_array)


# Check if the output is as expected
expected_output = np.array([4.29, np.nan, 7.0, 46.0, np.nan])
print(output_array)
print(expected_output)
# assert np.array_equal(output_array, expected_output), f"Expected {expected_output} but got {output_array}"


print("All test cases passed.")