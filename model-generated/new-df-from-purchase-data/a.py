import pandas as pd


data = [
    {'CustomerID': 1001, 'Product ID': 'A123', 'Price': 25.99, 'Purchase Date': '2023-12-01'},
    {'CustomerID': 1001, 'Product ID': 'B456', 'Price': 19.50, 'Purchase Date': '2023-12-05'},
    {'CustomerID': 1002, 'Product ID': 'A123', 'Price': 25.99, 'Purchase Date': '2023-11-10'},
    {'CustomerID': 1002, 'Product ID': 'C789', 'Price': 49.99, 'Purchase Date': '2023-11-15'},
    {'CustomerID': 1003, 'Product ID': 'B456', 'Price': 19.50, 'Purchase Date': '2023-12-12'},
    {'CustomerID': 1003, 'Product ID': 'C789', 'Price': 49.99, 'Purchase Date': '2023-12-12'},
    {'CustomerID': 1001, 'Product ID': 'A123', 'Price': 25.99, 'Purchase Date': '2023-12-20'},
]


# Create the pandas DataFrame
df = pd.DataFrame(data)


def calculate_customer_totals(df):
    # Group by CustomerID and sum the Price for each group
    customer_totals_df = df.groupby('CustomerID')['Price'].sum().reset_index()


    # Calculate average price per purchase
    avg_price_per_purchase = df['Price'].mean()


    return customer_totals_df,avg_price_per_purchase


customer_totals_df,avg_price_per_purchase=calculate_customer_totals(df)

assert len(customer_totals_df) == 3
assert customer_totals_df.loc[0,'CustomerID'] == 1001
assert round(avg_price_per_purchase, 2) == 30.99