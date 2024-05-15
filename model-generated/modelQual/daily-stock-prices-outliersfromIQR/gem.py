import pandas as pd
from scipy import stats

# Sample data (replace with your actual data loading)
data = {
    "Date": pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]),
    "Open": [100, 102, 101, 103],
    "High": [105, 108, 104, 109],
    "Low": [95, 98, 99, 101],
    "Close": [102, 105, 100, 107],
    "Volume": [10000, 12000, 8000, 15000]
}

df = pd.DataFrame(data)

# Calculate daily returns
df["Daily Return"] = (df["Close"] - df["Open"]) / df["Open"] * 100

# Identify outliers using IQR
iqr = stats.iqr(df["Daily Return"])
upper_bound = df["Daily Return"].median() + (1.5 * iqr)
lower_bound = df["Daily Return"].median() - (1.5 * iqr)
df["Outlier"] = ~((df["Daily Return"] >= lower_bound) & (df["Daily Return"] <= upper_bound))

# Calculate daily volatility
# df["Daily Volatility"] = df["Close"].std(rolling=1)

# Further analysis and visualization (optional)
# ...

print(df)  # Display the DataFrame with new columns