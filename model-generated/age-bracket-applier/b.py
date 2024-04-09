import pandas as pd
import numpy as np

# Define the age brackets
age_brackets = {
    "0-10": (0, 10),
    "11-18": (11, 18),
    "19-30": (19, 30),
    "31-50": (31, 50),
    "51-65": (51, 65),
    "66-80": (66, 80),
    "81-120": (81, 120)
}

# Create a function to determine the age bracket
def get_age_bracket(age):
    if pd.isna(age):
        return np.nan
    for bracket, (lower, upper) in age_brackets.items():
        if lower <= age <= upper:
            return bracket
    return np.nan

df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Apply the function to the Age column
df['Age_Bracket'] = df['Age'].apply(get_age_bracket)

# Print the updated DataFrame
print(df)