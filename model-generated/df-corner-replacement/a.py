import pandas as pd
import numpy as np


def replace_diagonals(df, val):
    # Get the number of rows and columns in the dataframe
    rows, cols = df.shape


    # Replace the main diagonal
    df.values[[np.arange(rows)]] = val


    # Replace the other diagonal
    df.values[:, [np.arange(cols)]] = val


    # Replace the top left and bottom right corners
    df.iloc[0, 0] = val
    df.iloc[rows-1, cols-1] = val


    # Replace the top right and bottom left corners
    df.iloc[0, cols-1] = val
    df.iloc[rows-1, 0] = val


    return df


# Create a random dataframe
df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))


# Replace the diagonals and corners with 0
df = replace_diagonals(df, 0)


print(df)