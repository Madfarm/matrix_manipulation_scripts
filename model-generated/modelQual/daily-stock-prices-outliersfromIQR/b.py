import pandas as pd
from scipy import stats

def find_outliers(data):
    # Create a new DataFrame
    df = pd.DataFrame(data)

    # Calculate daily returns
    df['Daily Return'] = (df['Close'] - df['Open']) * 100

    # Calculate the IQR
    iqr = stats.iqr(df['Daily Return'].dropna())

    # Calculate the upper and lower bounds
    lower_bound = df['Daily Return'].median() - 1.5 * iqr
    upper_bound = df['Daily Return'].median() + 1.5 * iqr

    # Find the outliers
    outliers = df[(df['Daily Return'] < lower_bound) | (df['Daily Return'] > upper_bound)]

    # Store the results in a dictionary
    result = {
        'Daily Return': df['Daily Return'],
        'Outliers': outliers
    }

    return result

data = {
    "Date": pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]),
    "Open": [100, 102, 101, 103],
    "High": [105, 108, 104, 109],
    "Low": [95, 98, 99, 101],
    "Close": [102, 105, 100, 107],
    "Volume": [10000, 12000, 8000, 15000]
}

result = find_outliers(data)

# Validate the output
assert len(result['Daily Return']) == 4
assert len(result['Outliers']) == 1
