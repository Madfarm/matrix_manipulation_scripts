import pandas as pd
import numpy as np


def replace_outliers(series):
    # Calculate the 5th and 95th percentile
    fifth_percentile = series.quantile(0.05)
    ninety_fifth_percentile = series.quantile(0.95)


    # Replace values lower than the 5th percentile with the 5th percentile value
    series = series.apply(lambda x: fifth_percentile if x < fifth_percentile else x)


    # Replace values greater than the 95th percentile with the 95th percentile value
    series = series.apply(lambda x: ninety_fifth_percentile if x > ninety_fifth_percentile else x)


    return series


# Create a sample series
ser = pd.Series(np.logspace(-2, 2, 30))


# Apply the function to the series
new_ser = replace_outliers(ser)


# Print the modified series
print(new_ser)