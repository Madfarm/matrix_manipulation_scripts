import pandas as pd
import numpy as np


# Create a data frame from the given input
data = {
    0: [17, 95, 13, 22, 28, 26, 82, 9],
    1: [74, 50, 68, 34, 33, 38, 62, 16],
    2: [93, 24, 31, 56, 59, 49, 96, 85],
    3: [4, 3, 41, 77, 10, 39, 77, 23],
    4: [20, 98, 26, 81, 21, 8, 77, 65],
    5: [34, 31, 16, 28, 49, 97, 43, 78],
    6: [44, 81, 9, 2, 62, 39, 38, 41],
    7: [24, 91, 75, 15, 48, 2, 88, 79],
    8: [2, 18, 60, 53, 49, 87, 69, 19],
    9: [61, 49, 66, 33, 80, 9, 99, 35]
}
df = pd.DataFrame(data)


# Ensure all values in the dataframe are numerical
assert df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all(), "The dataframe contains non-numerical values"


# Create a numpy series from the values that are greater than 62
series = df.values.flatten()
series = series[series > 62]


# Ensure the series is not empty
assert len(series) > 0, "The series is empty"


# Calculate the mean, median and standard deviation of the series
mean = round(np.mean(series), 2)
median = round(np.median(series), 2)
std_dev = round(np.std(series), 2)


# Ensure the calculated values are numbers
assert not np.isnan(mean) and not np.isnan(median) and not np.isnan(std_dev), "One or more calculations resulted in NaN"


# Output the sorted series and the calculated values
print("Sorted Series:")
print(np.sort(series))
print("\nCalculations:")
print({
    "Mean": mean,
    "Median": median,
    "Standard Deviation": std_dev
})