import pandas as pd
import numpy as np


def swap_columns(df, column1, column2):
    df[column1], df[column2] = df[column2], df[column1]
    return df


df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))


print("Original DataFrame:")
print(df)


print("\nDataFrame after swapping 'a' and 'c' columns:")
df = swap_columns(df, 'a', 'c')
print(df)


print("\nDataFrame after sorting columns in reverse alphabetical order:")
df = df.reindex(sorted(df.columns, reverse=True), axis=1)
print(df)