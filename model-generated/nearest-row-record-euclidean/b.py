import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({
    'p': [57, 68, 74, 80, 93, 69, 39, 63, 18, 79],
    'q': [77, 5, 40, 17, 48, 55, 23, 28, 4, 12],
    'r': [13, 92, 18, 39, 85, 8, 88, 25, 73, 45],
    's': [62, 24, 37, 60, 33, 11, 53, 61, 7, 34]
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


# Calculate the Euclidean distance between each pair of rows
distances = np.sqrt(np.sum((df.values[:, None] - df.values) ** 2, axis=2))


# Get the index of the nearest row for each row
nearest_row_index = np.argmin(distances, axis=1)


# Create a new column with the row number of the nearest row
df['nearest_row'] = nearest_row_index


# Print the resulting data frame
print(df)