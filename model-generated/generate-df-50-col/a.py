import pandas as pd
import numpy as np


# Define the data frame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Function to generate random data
def generate_random_data(df, rows):
    for i in range(rows):
        df = df.append({
            'Name': np.random.choice(['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu']),
            'GPA': np.random.uniform(2.0, 4.0),
            'Age': np.random.randint(20, 100),
            'Salary': np.random.randint(20000, 100000)
        }, ignore_index=True)
    return df


# Generate random data until the data frame has 50 rows
df = generate_random_data(df, 50 - len(df))


print(df)