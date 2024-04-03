import pandas as pd
import numpy as np


def replace_diagonals(df, val):
    # Create a mask to identify the diagonal elements
    mask = np.eye(df.shape[0], df.shape[1], dtype=bool)


    # Use the mask to replace the diagonal elements with the given value
    df.values[mask] = val


    return df


# Create a sample dataframe
df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))


# Define the value to replace the diagonals with
val = 0


# Call the function and print the result
print(replace_diagonals(df, val))