import pandas as pd
import numpy as np


# Define the data frame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Function to replace NaN with median and add a new column to track the changes
def replace_nan_with_median(df):
    # Create a new column 'had_nan' with all False values
    df['had_nan'] = False


    # Iterate over each column
    for col in df.columns:
        # Check if the column has NaN values
        if df[col].hasnans:
            # Replace NaN with the median of the column
            df[col].fillna(df[col].median(), inplace=True)


            # Set 'had_nan' to True for the rows where NaN was replaced
            df.loc[df[col].isin([df[col].median()]), 'had_nan'] = True


    return df


# Apply the function to the data frame
df = replace_nan_with_median(df)


# Print the updated data frame
print(df)