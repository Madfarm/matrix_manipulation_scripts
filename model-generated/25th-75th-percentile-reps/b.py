import numpy as np


def process_array(arr, repetitions):
    # Calculate the 25th and 75th percentile
    percentiles = np.percentile(arr, [25, 75])


    for _ in range(repetitions):
        # Set values between the 25th and 75th percentile to 0
        arr[(arr >= percentiles[0]) & (arr <= percentiles[1])] = 0

        assert np.all(arr[(arr >= percentiles[0]) & (arr <= percentiles[1])] == 0), "Values between the 25th and 75th percentile are not set to 0"

        # Randomly shuffle the array
        np.random.shuffle(arr)


    return arr


# Test the function
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
repetitions = 2


result = process_array(arr, repetitions)

assert len(np.unique(result)) > 1, "Array is not shuffled properly"