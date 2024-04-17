import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({
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
})


# Function to compute the correlation of each row with its succeeding row
def compute_correlation(df):
    correlations = []
    for i in range(len(df) - 1):
        row1 = df.iloc[i]
        row2 = df.iloc[i + 1]
        correlation = np.corrcoef(row1, row2)[0, 1]
        correlations.append(correlation)
    return correlations


# Compute the correlations
correlations = compute_correlation(df)

# Assertions to validate the output
assert abs(correlations[0] + 0.08294703564731044) < 1e-6
assert abs(correlations[1] + 0.18438820667085984) < 1e-6
assert abs(correlations[2] - 0.05215999211070559) < 1e-6
assert abs(correlations[3] + 0.5359817162968402) < 1e-6
assert abs(correlations[4] - 0.06369863994769666) < 1e-6
assert abs(correlations[5] + 0.5532625558444366) < 1e-6
assert abs(correlations[6] - 0.07613993772775804) < 1e-6