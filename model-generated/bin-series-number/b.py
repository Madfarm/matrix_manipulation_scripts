import pandas as pd
import numpy as np


# Create a sample series
ser = pd.Series(np.random.random(20))


# Define the bin names
bin_names = [f'Decile {i+1}' for i in range(10)]


# Bin the series into 10 equal deciles and replace the values with the bin name
binned_ser = pd.qcut(ser, q=10, labels=bin_names)


print(binned_ser)