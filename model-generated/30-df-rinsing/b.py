import pandas as pd


data = {
    'Orders': [1, 2, 3, 4, 50],
    'Inventory': [10, 20, 30, 430, 50],
    'Refunds': [100, 220, 300, 400, 500],
    'Turnover': [0.1, 0.2, 30.3, 70.4, 7.5],
    'Receipts': [6, 7, 80, 9, 10]
}


df = pd.DataFrame(data)


print("Before:")
print(df)


df.loc[df['Orders'] > 30, 'Orders'] = 30
df.loc[df['Inventory'] > 30, 'Inventory'] = 30
df.loc[df['Refunds'] > 30, 'Refunds'] = 30
df.loc[df['Turnover'] > 30, 'Turnover'] = 30
df.loc[df['Receipts'] > 30, 'Receipts'] = 30


print("After:")
print(df)