import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Define the function
def average_column(df, column, rows):
    return df.loc[rows, column].mean()


# Use the function
average = average_column(df, 'Salary', [1, 4])  # 1 and 4 are the indices of the second and last rows
print(average)