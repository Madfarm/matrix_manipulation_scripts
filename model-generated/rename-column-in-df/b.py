import pandas as pd
import numpy as np


def rename_column(df, column_name, new_name):
    if column_name in df.columns:
        df.rename(columns={column_name: new_name}, inplace=True)
    else:
        print(f"The column '{column_name}' does not exist in the data frame.")


# Test the function
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


rename_column(df, 'Name', 'Family Name')
print(df)