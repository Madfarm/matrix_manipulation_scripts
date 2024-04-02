import pandas as pd
import numpy as np


def find_second_largest(ser):
    # Calculate the mean
    mean = ser.mean()


    # Find values greater than the mean
    greater_than_mean = ser[ser > mean]


    # Find the 2nd largest value
    second_largest = greater_than_mean.nlargest(2).iloc[1]


    return second_largest


# Generate a random series
ser = pd.Series(np.random.randint(1, 100, 15))


# Find the 2nd largest value greater than the mean
second_largest = find_second_largest(ser)


print(f"Series: {ser.values}")
print(f"Mean: {ser.mean()}")
print(f"Second largest value greater than the mean: {second_largest}")