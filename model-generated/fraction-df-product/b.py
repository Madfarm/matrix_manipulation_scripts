import pandas as pd
import numpy as np


def calculate_product_and_reciprocal(df):
    # Validate inputs
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
    assert 'numerator' in df.columns and 'denominator' in df.columns, "DataFrame must contain 'numerator' and 'denominator' columns"
    assert (df['denominator'] != 0).all(), "Denominator cannot be zero"


    # Calculate the product of all fractions
    product = (df['numerator'] / df['denominator']).prod()


    # Calculate the reciprocal of each fraction
    df['reciprocal'] = df['denominator'] / df['numerator']


    return product, df


# Test the function
df = pd.DataFrame({
    'numerator': [1, 3, 5, 7, 9],
    'denominator': [2, 4, 15, 8, 10]
})


product, result_df = calculate_product_and_reciprocal(df)


print("Product of all fractions:", product)
print("DataFrame with reciprocals:")
print(result_df)