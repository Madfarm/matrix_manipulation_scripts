import numpy as np
import pandas as pd


# Define the data type for each field
dtype = [('position', [('x', float, 1), ('y', float, 1)]),
         ('color', [('r', float, 1), ('g', float, 1), ('b', float, 1)])]


# Create an empty structured array with any desired size
data_size = 10  # Adjust this value as needed
array = np.zeros(data_size, dtype=dtype)


# Access and modify elements using field names
array[0]['position']['x'] = 5.2
array[0]['position']['y'] = 1.8
array[0]['color']['r'] = 128
array[0]['color']['g'] = 0
array[0]['color']['b'] = 255


# Convert the structured array to a pandas DataFrame
df = pd.DataFrame(array)


# Add 4 additional rows generated at random
for i in range(4):
    df[-1] = (pd.DataFrame(np.random.rand(4, 5), columns=df.columns))


# Print the DataFrame
print(df)