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


assert np.isnan(output_array[1]), f"Expected output_array[1] to be np.nan, but got {output_array[1]}"
assert np.isnan(output_array[4]), f"Expected output_array[4] to be np.nan, but got {output_array[4]}"
assert output_array[0] == 4.29, f"Expected output_array[0] to be 4.29, but got {output_array[0]}"
assert output_array[2] == 7.0, f"Expected output_array[2] to be 7.0, but got {output_array[2]}"
assert output_array[3] == 46.0, f"Expected output_array[3] to be 46.0, but got {output_array[3]}"


print("All assertions passed.")