import pandas as pd
import numpy as np


# Define the dataframe
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Function to subtract mean from numerical columns
def subtract_mean(df):
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':  # Check if column is numerical
            mean = df[col].mean()  # Calculate mean
            df[col] = df[col].apply(lambda x: x - mean)  # Subtract mean from each entry
    return df


# Apply the function to the dataframe
df = subtract_mean(df)


print(df)