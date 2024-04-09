import pandas as pd
import numpy as np


# Define the function to replace nan values with the mean of the column
def replace_nan_with_mean(df):
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df['reversed_' + col] = df[col].apply(lambda x: x[::-1] if isinstance(x, str) else x)
    return df


# Create a sample DataFrame with nan values
df = pd.DataFrame({'Name': ['Seth', 'Esha', 'Jiametryc', 'Ash'],
                   'GPA': [2.4, 3.8, np.nan, np.nan], 
                   'Age': [30, 56, 8, np.nan],
                   'Salary': [np.nan, 80000, 41000, 33000],
                })


# Call the function to replace nan values with the mean of the column
df = replace_nan_with_mean(df)


# Print the updated DataFrame
print(df)