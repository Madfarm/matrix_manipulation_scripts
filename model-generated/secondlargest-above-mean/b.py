import pandas as pd
import numpy as np


def second_largest_above_mean(ser):
    # Calculate the mean
    mean_val = ser.mean()
    print(f"\nMean: {mean_val}")

    # Find values greater than the mean
    above_mean = ser[ser > mean_val]


    # Find the second largest value
    if len(above_mean) < 2:
        return None
    else:
        above_mean_sorted = above_mean.sort_values(ascending=True)
        return above_mean_sorted.iloc[1]


# Generate a random series
ser = pd.Series(np.random.randint(1, 100, 15))


# Print the series
print("Series:")
print(ser)


# Find and print the second largest value above the mean
second_largest = second_largest_above_mean(ser)
print("\nSecond largest value above the mean:", second_largest)