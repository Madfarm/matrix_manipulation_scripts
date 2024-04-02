import pandas as pd
import numpy as np


def reshape_series(ser):
    # Reshape the series into a 2D array with 7 columns and 5 rows
    arr = np.array(ser).reshape(5, 7)


    # Convert the 2D array into a DataFrame
    df = pd.DataFrame(arr)


    return df


# Generate a random series with 35 elements
ser = pd.Series(np.random.randint(1, 10, 35))


# Call the function and print the result
print(reshape_series(ser))