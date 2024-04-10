import numpy as np
import pandas as pd


# Define the data type for each field
dtype = [('position', [('x', float, 1), ('y', float, 1)]),
         ('color', [('r', int, 1), ('g', int, 1), ('b', int, 1)])]


# Create an empty structured array with any desired size
array = np.zeros(1, dtype=dtype)


# Access and modify elements using field names
array[0]['position']['x'] = 5.2
array[0]['position']['y'] = 1.8
array[0]['color']['r'] = 128
array[0]['color']['g'] = 0
array[0]['color']['b'] = 255


# Create a DataFrame from the structured array
df = pd.DataFrame(array)
print(df)


# Add 4 additional rows generated at random
# for i in range(4):
#     df.loc[-1] = pd.Series(({'position': {'x': np.random.uniform(0, 10), 'y': np.random.uniform(0, 10)},
#                               'color': {'r': np.random.uniform(0, 256), 'g': np.random.uniform(0, 256), 'b': np.random.uniform(0, 256)}}))
#     df.index = df.index + 1
#     df = df.sort_index()


# # Print the DataFrame
# print(df)