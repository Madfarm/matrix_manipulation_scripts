import pandas as pd
import numpy as np


# Create a sample DataFrame
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))


# Function to swap two columns in a DataFrame
def swap_columns(df, col1, col2):
    df[[col1, col2]] = df[[col2, col1]]
    return df


# Swap 'a' and 'c' columns
df = swap_columns(df, 'a', 'c')


# Sort columns in reverse alphabetical order
df = df.reindex(sorted(df.columns, reverse=True), axis=1)


print(df)