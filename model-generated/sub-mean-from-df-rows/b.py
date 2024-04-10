import pandas as pd
import numpy as np


def subtract_mean(df):
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] -= df[col].mean()
    return df


# Create the dataframe
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Print the original dataframe
print("Original DataFrame:")
print(df)


# Subtract the mean from every numerical column
df = subtract_mean(df)


# Print the resulting dataframe
print("\nDataFrame after subtracting the mean:")
print(df)