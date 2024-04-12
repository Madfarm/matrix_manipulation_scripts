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


def customer_purchases(df):


    # Group by CustomerID and calculate total amount spent and average price per purchase
    df_customer_purchases = (df.groupby('CustomerID')
        .agg(Total_Amount_Spent=('Price','sum'), Average_Price_Per_Purchase=('Price','mean'))
        .reset_index()
    )


    return df_customer_purchases


expected_output = pd.DataFrame({
   'CustomerID': [1001, 1002, 1003],
   'Total_Amount_Spent': [71.47999999999999, 75.98, 69.49000000000001],
   'Average_Price_Per_Purchase': [23.826666666666664, 37.990000, 34.745000000000005]
})


output_df = customer_purchases(df)
assert output_df.equals(expected_output), "Output does not match expected result"