import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Check if 'Name' and 'Salary' columns exist in the dataframe
if 'Name' in df.columns and 'Salary' in df.columns:
    # Multiply each row's salary value by the length of the name value
    df['Salary'] *= df['Name'].str.len()


print(df)