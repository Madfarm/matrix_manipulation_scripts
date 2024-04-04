import pandas as pd


# Define the standalone function
def func(num):
    return num + num


# Define the function that applies the standalone function to the dataframe
def apply_function(df, func):
    return df.apply(func)


# Create the dataframe
df = pd.DataFrame([[1, 5], [2, 6], [3, 7], [4, 8]], 
                  columns=["col_A", "col_B"])


# Apply the function to the dataframe
result = apply_function(df, func)


print(result)