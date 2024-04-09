import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({'Name': ['Seth', 'Esha', 'Jiametryc', 'Ash'],
                   'GPA': [2.4, 3.8, np.nan, np.nan], 
                   'Age': [30, 56, 8, np.nan],
                   'Salary': [np.nan, 80000, 41000, 33000],
                })


# Select rows 2 and 4
selected_rows = df.iloc[[1, 3]]


# Create a new data frame with a single row
new_df = pd.DataFrame(index=[0])


# Concatenate non-numerical values and add numerical values
for col in selected_rows.columns:
    if selected_rows[col].dtype == 'object':
        new_df[col] = ','.join(selected_rows[col].dropna().values)
    else:
        new_df[col] = selected_rows[col].sum()


print(new_df)