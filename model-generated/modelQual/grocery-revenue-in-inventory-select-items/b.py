import pandas as pd
from fractions import Fraction
import numpy as np

def calculate_inventory(df, product_names):
    # Initialize an empty list to store the calculated values
    calculated_values = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Check if the item matches any of the provided product names
        if row['Item'] in product_names:
            # Calculate the value by multiplying the price with the quantity
            value = float(row['Price']) * row['Quantity']
            calculated_values.append(value)
        else:
            # If the item doesn't match, insert a nan value
            calculated_values.append(np.nan)

    return calculated_values

# Define the input data
df = pd.DataFrame({
    'Item': ['Apples', 'Bananas', 'Oranges', 'Milk'],
    'Quantity': [5, 3, 4, 2],
    'Price': [Fraction(5, 4), Fraction(3, 4), Fraction(3, 2), Fraction(2)],
})
product_names = ['Oranges', 'Bananas']

# Calculate the inventory values
calculated_values = calculate_inventory(df, product_names)

# Define the expected output
expected_output = [np.nan, 9/4, 6, np.nan]

# Assert that the calculated values match the expected output
assert np.allclose(calculated_values, expected_output, equal_nan=True)