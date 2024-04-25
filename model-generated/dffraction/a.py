from fractions import Fraction
import pandas as pd
import scipy.stats as stats


def fraction_statistics(df):
    # Validate input
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
    assert all(col in df.columns for col in ['numerator', 'denominator']), "DataFrame must contain 'numerator' and 'denominator' columns"
    assert all(isinstance(val, (int, float)) for val in df['numerator'].values), "Numerator values must be numbers"
    assert all(isinstance(val, (int, float)) for val in df['denominator'].values), "Denominator values must be numbers"
    assert all(val != 0 for val in df['denominator'].values), "Denominator values cannot be zero"


    # Convert to fractions
    fractions = [Fraction(n, d) for n, d in zip(df['numerator'], df['denominator'])]


    # Calculate statistics
    sum_fractions = sum(fractions)
    mean_fractions = stats.mean(fractions)
    std_fractions = stats.std(fractions)


    # Validate output
    assert isinstance(sum_fractions, Fraction), "Sum of fractions must be a Fraction object"
    assert isinstance(mean_fractions, (int, float)), "Mean of fractions must be a number"
    assert isinstance(std_fractions, (int, float)), "Standard deviation of fractions must be a number"


    return sum_fractions, mean_fractions, std_fractions


# Test the function
df = pd.DataFrame({
    'numerator': [1, 3, 5, 7, 9],
    'denominator': [2, 4, 0, 8, 10]
})
print(fraction_statistics(df))