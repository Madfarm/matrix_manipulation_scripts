import pandas as pd


# Define the function
def func(num, index):
    return num + index


# Create the DataFrame
df = pd.DataFrame([[1, 5], [2, 6], [3, 7], [4, 8]], 
                  columns=["col_A", "col_B"])


# Apply the function to the entire DataFrame
df = df.apply(func, args=(df.index,))


print(df)