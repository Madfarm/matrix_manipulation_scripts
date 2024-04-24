import pandas as pd
import numpy as np


# Function to calculate daily returns
def calc_daily_returns(df):
    df['Daily Return'] = df['Close Price'].pct_change()
    return df


# Function to calculate average daily return
def calc_avg_daily_return(df):
    avg_daily_return = df['Daily Return'].mean()
    return avg_daily_return


# Function to calculate standard deviation of daily returns
def calc_std_dev(df):
    std_dev = df['Daily Return'].std()
    return std_dev


# Function to calculate maximum daily return
def calc_max_daily_return(df):
    max_daily_return = df['Daily Return'].max()
    return max_daily_return


# Load data
data = {
    'Date': ['2023-12-01', '2023-12-04', '2023-12-05', '2023-12-06', '2023-12-07'],
    'Close Price': [100.50, 98.75, 102.25, 101.00, 103.15]
}
df = pd.DataFrame(data)


# Calculate daily returns
df = calc_daily_returns(df)


# Calculate average daily return
avg_daily_return = calc_avg_daily_return(df)


# Calculate standard deviation of daily returns
std_dev = calc_std_dev(df)


# Calculate maximum daily return
max_daily_return = calc_max_daily_return(df)


# Assertions to verify calculations
assert np.isclose(avg_daily_return, 0.006773073122216533, atol=1e-5), "Average Daily Return calculation is incorrect"
assert np.isclose(std_dev, 0.0257, atol=1e-2), "Standard Deviation calculation is incorrect"
assert np.isclose(max_daily_return, 0.0354, atol=1e-2), "Maximum Daily Return calculation is incorrect"