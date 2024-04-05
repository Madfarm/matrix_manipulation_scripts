import pandas as pd


# Create a DataFrame
data = {
    'Orders': [1, 2, 3, 4, 50],
    'Inventory': [10, 20, 30, 430, 50],
    'Refunds': [100, 220, 300, 400, 500],
    'Turnover': [0.1, 0.2, 30.3, 70.4, 7.5],
    'Receipts': [6, 7, 80, 9, 10]
}
df = pd.DataFrame(data)


# Use the apply function to apply a function to each column
df = df.apply(lambda x: x.where(x <= 30, 30))


print(df)