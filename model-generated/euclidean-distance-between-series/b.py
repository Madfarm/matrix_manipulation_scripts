import pandas as pd
import numpy as np


def euclidean_distance(p, q):
    # Check if the series have the same length
    if len(p) != len(q):
        raise ValueError("Series must be the same length")


    # Calculate the squared difference between each pair of corresponding elements
    diff_squared = (p - q) ** 2


    # Calculate the sum of the squared differences
    sum_squared = diff_squared.sum()


    # Take the square root of the sum to get the Euclidean distance
    distance = np.sqrt(sum_squared)


    return distance


p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


print(euclidean_distance(p, q))