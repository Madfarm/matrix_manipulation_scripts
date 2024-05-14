import pandas as pd
import numpy as np
from fractions import Fraction


# Creating DataFrame
df = pd.DataFrame({
    'Item': ['Apples', 'Bananas', 'Oranges', 'Milk'],
    'Quantity': [5, 3, 4, 2],
    'Price': [Fraction(5, 4), Fraction(3, 4), Fraction(3, 2), Fraction(2)],
})

print(df)

sensor_data = pd.Series([
    [0.1, 0.2, np.nan, 0.4],
    [0.5, 0.6, 0.7, 0.8],
    [0.9, np.nan, 1.1, 1.2],
    [1.3, 1.4, 1.5, 1.6]
])

print(sensor_data)