import pandas as pd
import numpy as np


def calculate_range_IQR_CV(df):
    # Select numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns


    # Create a new DataFrame to store the results
    result_df = pd.DataFrame(index=numeric_cols, columns=['Range', 'IQR', 'CV'])


    # Iterate over each numeric column and calculate the range, IQR, and CV
    for col in numeric_cols:
        # Calculate the range
        min_val = df[col].min()
        max_val = df[col].max()
        range_val = max_val - min_val


        # Calculate the IQR
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1


        # Calculate the CV
        mean = df[col].mean()
        std_dev = df[col].std()
        cv = std_dev / mean if mean != 0 else np.nan


        # Store the results in the new DataFrame
        result_df.loc[col, 'Range'] = range_val
        result_df.loc[col, 'IQR'] = iqr
        result_df.loc[col, 'CV'] = cv


    # Validate the interquartile range
    assert (result_df['IQR'] >= 0).all(), "Interquartile range cannot be negative"


    # Validate the coefficient of variation
    assert (result_df['CV'] >= 0).all(), "Coefficient of variation cannot be negative"


    return result_df


# Example usage
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [15, 25, 35, 45, 55],
    'C': [20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)


result_df = calculate_range_IQR_CV(df)
print(result_df)