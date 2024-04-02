import pandas as pd
import numpy as np


def replace_outliers(series):
    # Calculate the 5th and 95th percentile
    fifth_percentile = series.quantile(0.05)
    ninety_fifth_percentile = series.quantile(0.95)


    # Replace values lower than the 5th percentile with the 5th percentile value
    series.loc[series < fifth_percentile] = fifth_percentile


    # Replace values greater than the 95th percentile with the 95th percentile value
    series.loc[series > ninety_fifth_percentile] = ninety_fifth_percentile


    return series


# Create a series
ser = pd.Series(np.logspace(-2, 2, 30))


# Call the function
result = replace_outliers(ser)


print(result)