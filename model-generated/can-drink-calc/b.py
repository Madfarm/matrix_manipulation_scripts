import pandas as pd
import numpy as np


def check_age(df):
    if 'Age' in df.columns:
        df['can_drink'] = df['Age'] >= 21
    return df


# Test the function
df = pd.DataFrame({'Name': ['Seth', 'Esha', 'Jiametryc', 'Ash'],
                   'GPA': [2.4, 3.8, np.nan, np.nan], 
                   'Age': [30, 56, 8, np.nan],
                   'Salary': [np.nan, 80000, 41000, 33000],
                })


print(check_age(df))