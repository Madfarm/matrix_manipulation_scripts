import numpy as np


def calculate_mad(data):
    # Calculate the median
    median = np.median(data)


    # Calculate the absolute deviations from the median
    deviations = np.abs(data - median)


    # Calculate the median absolute deviation
    mad = np.median(deviations)


    return mad


# Test the function
data = np.array([25,565,45,67,12,78,56,32,57,78,12,34,123,377,211,93,194,472])
print(calculate_mad(data))