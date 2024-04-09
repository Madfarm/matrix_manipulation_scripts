import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({'Name': ['Seth', 'Esha', 'Jiametryc', 'Ash'],
                   'GPA': [2.4, 3.8, np.nan, np.nan], 
                   'Age': [30, 56, 8, np.nan],
                   'Salary': [np.nan, 80000, 41000, 33000],
                })


# Select rows 2 and 4
rows = df.iloc[[2, 4]]


# Initialize a new data frame with a single row
new_df = pd.DataFrame(index=[0])


# Iterate over each column
for col in rows.columns:
    # If the column contains non-numerical values, concatenate them
    if rows[col].dtype == 'object':
        new_df[col] = rows[col].str.cat(sep=' ')
    # If the column contains numerical values, add them together
    else:
        new_df[col] = rows[col].sum()


print(new_df)