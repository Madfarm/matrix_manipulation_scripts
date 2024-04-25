import pandas as pd
import numpy as np


def preprocess_dataset(df):
    # Fill missing values with the mean of their respective columns
    df = df.fillna(df.mean())


    # Remove outliers from each column
    for col in df.columns:
        df = df[np.abs(df[col] - df[col].mean()) <= (2 * df[col].std())]


    # Calculate the mean, median, and standard deviation for each numeric column
    means = df.mean()
    medians = df.median()
    stds = df.std()


    return means, medians, stds


data = {
    'A': [10, 20, np.nan, 40, 200],
    'B': [15, np.nan, 35, 45, 55],
    'C': [20, 30, 40, np.nan, 60]
}
df = pd.DataFrame(data)


means, medians, stds = preprocess_dataset(df)


# Assertions to validate the calculations
assert np.allclose(means.values, [40.0, 40.0, 40.0])
assert np.allclose(medians.values, [40.0, 40.0, 40.0])
assert np.allclose(stds.values, [0.0, 0.0, 0.0])