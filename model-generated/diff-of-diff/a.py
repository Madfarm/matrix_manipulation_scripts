import pandas as pd
import numpy as np


# Create a series
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])


# Calculate the first difference
diff1 = ser.diff()


# Calculate the second difference
diff2 = diff1.diff()


# Print the results
print(diff1)
print(diff2)
