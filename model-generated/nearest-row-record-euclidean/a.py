import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({
    'p': [57, 68, 74, 80, 93, 69, 39, 63, 18, 79],
    'q': [77, 5, 40, 17, 48, 55, 23, 28, 4, 12],
    'r': [13, 92, 18, 39, 85, 8, 88, 25, 73, 45],
    's': [62, 24, 37, 60, 33, 11, 53, 61, 7, 34]
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


# Function to calculate the euclidean distance between two vectors
def euclidean_distance(vector1, vector2):
    return np.sqrt(sum((vector1 - vector2) ** 2))


# Create a new column to store the row number of the nearest row-record
df['nearest_row'] = 0


# Iterate over each row in the data frame
for i in range(len(df)):
    min_distance = float('inf')
    nearest_row = None


    # Iterate over each other row in the data frame
    for j in range(len(df)):
        if i != j:
            distance = euclidean_distance(df.iloc[i], df.iloc[j])


            # Update the minimum distance and the nearest row if necessary
            if distance < min_distance:
                min_distance = distance
                nearest_row = j


    # Store the row number of the nearest row-record
    df.loc[df.index[i], 'nearest_row'] = nearest_row


# Print the resulting data frame
print(df)


# Validate the calculations using assertions
assert df.loc['a', 'nearest_row'] == 2
assert df.loc['b', 'nearest_row'] == 6
assert df.loc['c', 'nearest_row'] == 7
assert df.loc['d', 'nearest_row'] == 7
assert df.loc['e', 'nearest_row'] == 1
assert df.loc['f', 'nearest_row'] == 2
assert df.loc['g', 'nearest_row'] == 1
assert df.loc['h', 'nearest_row'] == 3
assert df.loc['i', 'nearest_row'] == 6
assert df.loc['j', 'nearest_row'] == 3