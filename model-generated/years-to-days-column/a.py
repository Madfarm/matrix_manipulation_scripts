import pandas as pd
import numpy as np


def convert_years_to_days(df, column_name):
    # Ensure the column exists in the dataframe
    if column_name not in df.columns:
        raise ValueError(f"The column '{column_name}' does not exist in the dataframe.")


    # Convert the column from years to days
    df[column_name] = df[column_name] * 365


    return df


# Create a sample dataframe
df = pd.DataFrame({'Name': ['Seth', 'Esha', 'Jiametryc', 'Ash'],
                   'GPA': [2.4, 3.8, np.nan, np.nan], 
                   'Age': [30, 56, 8, np.nan],
                   'Salary': [np.nan, 80000, 41000, 33000],
                })


# Specify the column to convert
column_name = 'Age'


# Convert the column from years to days
df = convert_years_to_days(df, column_name)


# Print the updated dataframe
print(df)