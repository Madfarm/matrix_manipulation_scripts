import pandas as pd
from fractions import Fraction


# Creating DataFrame
df = pd.DataFrame({
    'Item': ['Apples', 'Bananas', 'Oranges', 'Milk'],
    'Quantity': [5, 3, 4, 2],
    'Price': [Fraction(5, 4), Fraction(3, 4), Fraction(3, 2), Fraction(2)],
})

print(df)