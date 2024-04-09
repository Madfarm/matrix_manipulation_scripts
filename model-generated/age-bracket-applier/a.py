import pandas as pd
import numpy as np


df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


def get_age_bracket(age):
    if pd.isnull(age):
        return np.nan
    elif 0 <= age <= 10:
        return "0-10"
    elif 11 <= age <= 18:
        return "11-18"
    elif 19 <= age <= 30:
        return "19-30"
    elif 31 <= age <= 50:
        return "31-50"
    elif 51 <= age <= 65:
        return "51-65"
    elif 66 <= age <= 80:
        return "66-80"
    elif 81 <= age <= 120:
        return "81-120"
    else:
        return np.nan


df['Age_Bracket'] = df['Age'].apply(get_age_bracket)


print(df)