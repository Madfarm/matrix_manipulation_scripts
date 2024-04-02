import pandas as pd
import numpy as np


def reshape_series(ser):
    # Reshape the series into a numpy array with 7 columns and 5 rows
    arr = ser.values.reshape((5, 7))


    # Create a data frame from the numpy array
    df = pd.DataFrame(arr)


    return df


# Generate a random series
ser = pd.Series(np.random.randint(1, 10, 35))


# Call the function and print the result
print(reshape_series(ser))