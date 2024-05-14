import pandas as pd
from fractions import Fraction
import scipy.stats as stats


def fraction_statistics(df):
    # Validate input
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
    assert 'numerator' in df.columns and 'denominator' in df.columns, "DataFrame must contain 'numerator' and 'denominator' columns"
    assert all(df['denominator'] != 0), "Denominator cannot be zero"


    # Convert to fractions and compute statistics
    fractions = df.apply(lambda row: Fraction(row['numerator'], row['denominator']), axis=1)
    sum_of_fractions = sum(fractions)
    mean_of_fractions = stats.tmean(fractions)
    std_dev_of_fractions = stats.tstd(fractions)


    # Validate output
    assert isinstance(sum_of_fractions, Fraction), "Sum of fractions must be a Fraction object"
    assert isinstance(mean_of_fractions, Fraction), "Mean of fractions must be a float"
    assert isinstance(std_dev_of_fractions, float), "Standard deviation of fractions must be a float"


    return sum_of_fractions, mean_of_fractions, std_dev_of_fractions


# Example usage:
df = pd.DataFrame({
    'numerator': [1, 3, 5, 7, 9],
    'denominator': [2, 4, 1, 8, 10]
})


print(fraction_statistics(df))