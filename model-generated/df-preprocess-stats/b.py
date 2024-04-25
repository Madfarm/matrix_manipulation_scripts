import pandas as pd
import numpy as np


def preprocess_data(df):
    # Fill missing values with the mean of their respective columns
    df = df.fillna(df.mean())


    # Remove outliers from each column
    for col in df.columns:
        mean = df[col].mean()
        std_dev = df[col].std()
        df = df[(df[col] >= mean - 2 * std_dev) & (df[col] <= mean + 2 * std_dev)]


    # Calculate the mean, median, and standard deviation for each numeric column
    calculations = {}
    for col in df.columns:
        calculations[col] = {
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std_dev': df[col].std()
        }


    return df, calculations


data = {
    'A': [10, 20, np.nan, 40, 200],
    'B': [15, np.nan, 35, 45, 55],
    'C': [20, 30, 40, np.nan, 60]
}
df = pd.DataFrame(data)


df, calculations = preprocess_data(df)

# Assertions to validate the calculations
assert round(calculations['A']['mean'], 4) == 67.5, "Incorrect mean for column A"
assert calculations['A']['median'] == 40, "Incorrect median for column A"
assert round(calculations['A']['std_dev'], 4) == 77.2577, "Incorrect standard deviation for column A"


assert round(calculations['B']['mean'], 4) == 37.5, "Incorrect mean for column B"
assert calculations['B']['median'] == 37.5, "Incorrect median for column B"
assert round(calculations['B']['std_dev'], 4) == 14.7902, "Incorrect standard deviation for column B"


assert round(calculations['C']['mean'], 4) == 37.5, "Incorrect mean for column C"
assert calculations['C']['median'] == 37.5, "Incorrect median for column C"
assert round(calculations['C']['std_dev'], 4) == 14.7902, "Incorrect standard deviation for column C"