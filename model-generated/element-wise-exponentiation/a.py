import numpy as np


def calculate_stats(arr):
    # Calculate the element-wise exponentiation of the array
    arr_exp = np.exp(arr)
    np.testing.assert_allclose([ 7.3890561, 20.08553692, 54.59815003], arr_exp, atol=1e-6)

    # Truncate the values to two decimals
    arr_truncated = np.round(arr_exp, 2)
    assert (arr_truncated == [ 7.39, 20.09, 54.6 ]).all()

    # Calculate the mean, median, and standard deviation
    mean = np.mean(arr_truncated)
    median = np.median(arr_truncated)
    std_dev = np.std(arr_truncated)


    # Store the results in a dictionary
    stats = {
        "mean": mean,
        "median": median,
        "std_dev": std_dev
    }


    return stats


# Test the function with the input [2,3,4]
input_array = np.array([2,3,4])
stats = calculate_stats(input_array)

assert stats == {'mean': 27.36, 'median': 20.09, 'std_dev': 19.947191949411494}