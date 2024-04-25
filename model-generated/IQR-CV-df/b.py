import pandas as pd
import numpy as np


def calculate_range_IQR_CV(df):
    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=[np.number])


    # Calculate range, IQR, and CV for each numeric column
    output_df = pd.DataFrame({
        'Range': numeric_cols.apply(lambda x: x.max() - x.min()),
        'IQR': numeric_cols.apply(lambda x: x.quantile(0.75) - x.quantile(0.25)),
        'CV': numeric_cols.apply(lambda x: x.std() / x.mean())
    })


    # Validate IQR and CV calculations
    assert np.all(output_df['IQR'] >= 0), "IQR cannot be negative"
    assert np.all(output_df['CV'] >= 0), "CV cannot be negative"


    return output_df


# Test the function
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [15, 25, 35, 45, 55],
    'C': [20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
result_df = calculate_range_IQR_CV(df)
print(result_df)