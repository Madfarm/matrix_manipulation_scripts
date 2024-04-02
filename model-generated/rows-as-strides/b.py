import pandas as pd
import numpy as np


def series_to_strides(s, stride=1):
    if not isinstance(s, pd.Series):
        raise ValueError("Input must be a pandas Series")
    if stride < 1:
        raise ValueError("Stride must be a positive integer")


    # Get the array representation of the series
    arr = s.values


    # Calculate the number of strides
    num_strides = (len(arr) - 1) // stride + 1


    # Initialize the output list
    output = []


    # Iterate over the strides
    for i in range(num_strides):
        # Get the start and end indices for this stride
        start = i * stride
        end = min(start + stride, len(arr))


        # Append the stride to the output list
        output.append(arr[start:end])


    # Convert the output list to a DataFrame
    df = pd.DataFrame(output)


    return df


L = pd.Series(range(15))
print(series_to_strides(L))