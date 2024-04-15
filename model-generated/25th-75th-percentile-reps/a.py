import numpy as np


def set_percentile_to_zero(arr, repetitions):
    for _ in range(repetitions):
        # Calculate the 25th and 75th percentile
        q1 = np.percentile(arr, 25)
        q3 = np.percentile(arr, 75)


        # Set values between q1 and q3 to 0
        arr[(arr >= q1) & (arr <= q3)] = 0


        assert np.all(result[result != 0] >= np.percentile(arr, 75)) or np.all(result[result != 0] <= np.percentile(arr, 25))

        # Randomly shuffle the array
        np.random.shuffle(arr)


    return arr


# Test the function
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
repetitions = 2
result = set_percentile_to_zero(arr, repetitions)


# Assertions to validate the output
assert np.count_nonzero(result == 0) >= repetitions * len(arr) // 2



print("All assertions passed.")