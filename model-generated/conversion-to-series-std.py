import pandas as pd
import numpy as np


def find_indices(array):
    # Find the indices of non-zero elements
    indices = np.nonzero(array)[0]


    # Create a series from the indices
    series = pd.Series(indices)


    # Calculate the standard deviation of the series
    std_dev = series.std()


    return series, std_dev


# Example usage:
array = [1,0,0,3,4,0,0,5,4,0,0,0,3,0,0,4,0,2,0,5,6,1,1]
series, std_dev = find_indices(array)


print("Series of indices:", series)
print("Standard deviation:", std_dev)