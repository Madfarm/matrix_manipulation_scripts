import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Find rows with nan values
nan_rows = df[df.isnull().any(axis=1)]



# Remove rows with nan values
df = df.dropna()


# Add values from nan rows to remaining rows
for index, row in nan_rows.iterrows():
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] += row[col]


print(df)