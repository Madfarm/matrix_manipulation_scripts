import pandas as pd

# Define the data
data = {
    "Date": ["2023-12-08", "2024-01-08", "2024-02-08", "2024-03-08", "2024-04-08", "2024-05-08", "2024-06-08"],
    "Vein Ripper": [24.64, 24.10, 25.00, 24.75, 24.50, 24.90, 24.30],
    "Tinybones, the Pickpocket": [14.84, 14.50, 15.00, 14.70, 14.40, 14.60, 14.20],
    "Tarmogoyf": [11.12, 11.50, 11.00, 11.20, 11.40, 11.10, 11.00]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Calculate the daily returns
daily_returns = df.pct_change()

# Calculate the average daily return
average_daily_return = daily_returns.mean()

# Print the average daily return
print("Average Daily Return:")
print(average_daily_return)

# Calculate the standard deviation of daily returns
std_dev_daily_return = daily_returns.std()

# Print the standard deviation of daily returns
print("\nStandard Deviation of Daily Returns:")
print(std_dev_daily_return)

# Calculate the Sharpe ratio
sharpe_ratio = average_daily_return / std_dev_daily_return

# Print the Sharpe ratio
print("\nSharpe Ratio:")
print(sharpe_ratio)

# Determine which card is most likely to increase in price
most_likely_to_increase = sharpe_ratio.idxmax()

# Print the result
print(f"\nThe card most likely to increase in price is: {most_likely_to_increase}")