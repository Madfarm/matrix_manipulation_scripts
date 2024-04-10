import pandas as pd
import numpy as np


def process_array(arr):
    # Negate all elements above 100
    arr = [-x if x > 100 else x for x in arr]


    # Convert the array into a pandas Series
    series = pd.Series(arr)


    # Calculate the mean, median, and standard deviation
    mean = series.mean()
    median = series.median()
    std_dev = series.std()


    # Return the series and the statistics in a dictionary
    return series, {'mean': mean, 'median': median, 'std_dev': std_dev}


# Test the function
arr = [45,43,67,72,81,80,112,92,97,98,127,94,91,35,76,62,183,79,81,199,151]
series, stats = process_array(arr)


# Print the series and the statistics
print("Series:")
print(series)
print("\nStatistics:")
print(stats)