import numpy as np


def median_absolute_deviation(series):
    median = np.median(series)
    deviations = np.abs(series - median)
    mad = np.median(deviations)
    return mad


# Input series
series = np.array([25,565,45,67,12,78,56,32,57,78,12,34,123,377,211,93,194,472])


# Calculate and print the median absolute deviation
mad = median_absolute_deviation(series)
print(f"Median Absolute Deviation: {mad}")