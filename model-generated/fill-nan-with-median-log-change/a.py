import pandas as pd
import numpy as np


# Create the DataFrame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Create a new column 'had_nan' with False values
df['had_nan'] = False


# Iterate over each column in the DataFrame
for col in df.columns:
    # Check if the column is not 'had_nan'
    if col != 'had_nan':
        # Fill NaN values with the median of the column
        df[col] = df[col].fillna(df[col].median())


        # Set 'had_nan' to True for rows where NaN was replaced
        df.loc[df[col].isnull(), 'had_nan'] = True


print(df)