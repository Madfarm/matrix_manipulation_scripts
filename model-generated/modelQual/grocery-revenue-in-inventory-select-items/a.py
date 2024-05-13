import pandas as pd
from fractions import Fraction
import numpy as np

def calculate_inventory_value(df, product_names):
    # Initialize an empty list to store the total value of each item
    total_values = []

    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        # Check if the item name matches any of the provided product names
        if row['Item'] in product_names:
            # Calculate the total value by multiplying the price with the quantity
            total_value = float(row['Price']) * row['Quantity']
            total_values.append(total_value)
        else:
            # If the item name does not match, insert a nan value
            total_values.append(np.nan)

    return total_values

# Test the function
df = pd.DataFrame({
    'Item': ['Apples', 'Bananas', 'Oranges', 'Milk'],
    'Quantity': [5, 3, 4, 2],
    'Price': [Fraction(5, 4), Fraction(3, 4), Fraction(3, 2), Fraction(2)],
})
product_names = ['Oranges', 'Bananas']

assert calculate_inventory_value(df, product_names) == [np.nan, 0.75 * 3, 1.5 * 4, np.nan], "Output does not match expected output"