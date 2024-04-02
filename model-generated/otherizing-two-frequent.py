import numpy as np
import pandas as pd


# Create a random series
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))


# Find the top 2 most frequent items
top_2 = ser.value_counts().index[:2]


# Replace everything else with 'Other'
ser[~ser.isin(top_2)] = 'Other'


print(ser)