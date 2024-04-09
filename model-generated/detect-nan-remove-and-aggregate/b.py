import pandas as pd
import numpy as np


# Define the data frame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Function to remove rows with NaN values and add numeric values to remaining rows
def remove_nan_and_add(df):
    # Find rows with NaN values
    nan_rows = df[df.isnull().any(axis=1)]
    print(nan_rows)

    running_totals = {
        'Age': 0,
        'Salary': 0,
        'GPA': 0.0
    }
    for row in nan_rows:
        running_totals[row] += nan_rows[row]

    # Remove rows with NaN values
    df_clean = df.drop(nan_rows.index)


    print(running_totals)
    # Add numeric values to remaining rows
    for col in df_clean.columns:
        if pd.api.types.is_numeric_dtype(df_clean[col]):
            df_clean[col] += df[col].sum()


    return df_clean


# Apply the function to the data frame
df_clean = remove_nan_and_add(df)


# Print the cleaned data frame
print(df_clean)