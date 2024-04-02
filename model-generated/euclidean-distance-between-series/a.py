import pandas as pd
import numpy as np


def euclidean_distance(p, q):
    return np.sqrt(sum((p - q) ** 2))


p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


print(euclidean_distance(p, q))