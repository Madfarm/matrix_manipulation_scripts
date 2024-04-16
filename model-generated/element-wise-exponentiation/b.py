import numpy as np


def calculate_statistics(arr):
    # Calculate the element-wise exponentiation of the array
    arr_exp = np.exp(arr)


    # Truncate the values to two decimals
    arr_truncated = np.round(arr_exp, 2)


    # Calculate the mean, median, and standard deviation
    mean = np.mean(arr_truncated)
    median = np.median(arr_truncated)
    std = np.std(arr_truncated)


    # Store the results in a dictionary
    statistics = {
        'mean': mean,
        'median': median,
        'std': std
    }


    return statistics


# Test the function with the input [2, 3, 4]
input_arr = [2, 3, 4]
statistics = calculate_statistics(input_arr)

