import pandas as pd
import numpy as np


def calculate_product_and_reciprocal(df):
    # Validate input
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
    assert set(df.columns) == {'numerator', 'denominator'}, "DataFrame must contain 'numerator' and 'denominator' columns"
    assert df['denominator'].ne(0).all(), "Denominator cannot be zero"


    # Calculate product of all fractions
    product = (df['numerator'] / df['denominator']).prod()


    # Calculate reciprocal of each fraction
    reciprocal_df = pd.DataFrame({'reciprocal_numerator': df['denominator'], 'reciprocal_denominator': df['numerator']})


    # Validate output
    assert isinstance(product, (int, float)), "Product must be a number"
    assert isinstance(reciprocal_df, pd.DataFrame), "Reciprocal result must be a pandas DataFrame"
    assert set(reciprocal_df.columns) == {'reciprocal_numerator', 'reciprocal_denominator'}, "Reciprocal result must contain 'reciprocal_numerator' and 'reciprocal_denominator' columns"


    return product, reciprocal_df


# Create a DataFrame
df = pd.DataFrame({
    'numerator': [1, 3, 5, 7, 9],
    'denominator': [2, 4, 15, 8, 10]
})


# Call the function
product, reciprocal_df = calculate_product_and_reciprocal(df)