import pandas as pd
import numpy as np


# Create the DataFrame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 0], 
                   'Age': [30, 56, 8, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Define a function to process the DataFrame
def process_dataframe(df):
    # For each row in the DataFrame
    for i in range(len(df)):
        # If the value in the 'Age' column is 0
        if df.loc[i, 'Age'] == 0:
            # For each column in the DataFrame
            for col in df.columns:
                # If the value is numerical
                if pd.api.types.is_numeric_dtype(df[col]):
                    # Set the value to NaN
                    df.loc[i, col] = np.nan
                else:
                    # Set the value to 'error'
                    df.loc[i, col] = 'error'
    return df


# Process the DataFrame
df = process_dataframe(df)


# Print the processed DataFrame
print(df)


