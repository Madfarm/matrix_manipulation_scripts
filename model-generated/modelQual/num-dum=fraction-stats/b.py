import pandas as pd
from fractions import Fraction
import math

def calculate_fraction_stats(df):
    # Combine numerators and denominators to make proper Fraction values
    fractions = df.apply(lambda row: Fraction(row['numerator'], row['denominator']), axis=1)

    # Calculate the mean, sum, and standard deviation of these resulting values
    mean = (sum(fractions) / len(fractions)) * 1.0
    total = sum(fractions) * 1.0
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in fractions) / len(fractions))

    # Return those calculations organized in a dictionary
    return {
        'mean': mean,
        'sum': total,
        'std_dev': std_dev
    }

# Test the function
df = pd.DataFrame({
    'numerator': [1, 3, 5, 7, 9],
    'denominator': [2, 4, 1, 8, 10]
})

result = calculate_fraction_stats(df)

# Assertions to validate the final dictionary's values
assert math.isclose(result['mean'], 1.605), f"Expected mean to be approximately 1.516, but got {result['mean']}"
assert math.isclose(result['sum'], 8.025), f"Expected sum to be approximately 7.58, but got {result['sum']}"
assert math.isclose(result['std_dev'], 1.7034083479894069), f"Expected std_dev to be approximately 1.9425, but got {result['std_dev']}"