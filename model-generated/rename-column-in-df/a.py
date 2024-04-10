import pandas as pd
import numpy as np


def rename_column(df, column_name, new_name):
    df = df.copy()
    df.rename(columns={column_name: new_name}, inplace=True)
    return df


# Test the function
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


print("Before renaming:")
print(df)


df = rename_column(df, 'Name', 'Family Name')


print("After renaming:")
print(df)