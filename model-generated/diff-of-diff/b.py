import pandas as pd
import numpy as np


# Create a pandas series
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])


# Calculate the difference between consecutive numbers
diff = ser.diff()


# Calculate the difference of differences
diff_of_diff = diff.diff()


# Print the results
print(diff)
print(diff_of_diff)