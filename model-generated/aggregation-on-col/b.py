import pandas as pd
import numpy as np


# Define the dataframe
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Define the aggregation functions
aggregation_functions = ['mean', 'min', 'max', 'std']


# Define the column to aggregate
column = 'Salary'


# Create an empty dictionary to store the results
results = {}


# Iterate over the aggregation functions
for func in aggregation_functions:
    # Apply the aggregation function to the column
    result = getattr(df[column], func)()


    # Store the result in the dictionary
    results[func] = result


# Print the results
print(results)