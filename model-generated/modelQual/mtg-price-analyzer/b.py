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
df_returns = df.pct_change()

# Calculate the mean returns
mean_returns = df_returns.mean()

# Print the mean returns
print(mean_returns)