import pandas as pd
import numpy as np


# Create a data frame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 3.2], 
                   'Age': [30, 56, 8, np.nan, 0],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Function to check if a value is numeric
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Function to process a row
def process_row(row):
    if row['Age'] == 0 or 0.0:
        for column, value in row.items():
            print(column + ", " + value)
            if is_numeric(value):
                row[column] = np.nan
            else:
                row[column] = 'error'
    return row


# Apply the process_row function to each row in the data frame
df = df.apply(process_row, axis=1)


print(df)