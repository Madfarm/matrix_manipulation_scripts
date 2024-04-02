import pandas as pd
import numpy as np


# Create a sample series
ser = pd.Series(np.random.random(20))


# Define the bin names
bin_names = ['bin_0', 'bin_1', 'bin_2', 'bin_3', 'bin_4', 'bin_5', 'bin_6', 'bin_7', 'bin_8', 'bin_9']


# Bin the series into 10 equal deciles and replace the values with the bin name
binned_ser = pd.qcut(ser, q=10, labels=bin_names, duplicates='drop')


print(binned_ser)