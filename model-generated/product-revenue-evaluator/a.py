import pandas as pd


def calculate_revenue(data):
    # Create the pandas DataFrame
    df = pd.DataFrame(data)


    # Calculate revenue for each order and add it to the dataframe
    df['Revenue'] = df['Price'] * df['Quantity']


    # Group by product ID, sum up revenues, then find max value index
    most_profitable_product_id = df.groupby('Product ID')['Revenue'].sum().idxmax()


    average_amount_of_each_product = df.groupby("Product Name")["Revenue"].mean()


    result = {
        "product_generated_most_revenue": most_profitable_product_id,
        "average_amount_of_each_product": dict(average_amount_of_each_product)
    }
    return result


data = [
    {'Order ID': 100, 'Customer ID': 123, 'Product ID': 'P1', 'Product Name': 'Phone Case', 'Order Date': '2024-01-10', 'Price': 14.99, 'Quantity': 2},
    {'Order ID': 101, 'Customer ID': 123, 'Product ID': 'P2', 'Product Name': 'Headphones', 'Order Date': '2024-01-10', 'Price': 79.99, 'Quantity': 1},
    {'Order ID': 102, 'Customer ID': 456, 'Product ID': 'P3', 'Product Name': 'Smartwatch', 'Order Date': '2024-01-15', 'Price': 199.99, 'Quantity': 1},
    {'Order ID': 103, 'Customer ID': 123, 'Product ID': 'P2', 'Product Name': 'Headphones', 'Order Date': '2024-02-01', 'Price': 79.99, 'Quantity': 1},
    {'Order ID': 104, 'Customer ID': 789, 'Product ID': 'P1', 'Product Name': 'Phone Case', 'Order Date': '2024-02-05', 'Quantity': 1},
]


result = calculate_revenue(data)

assert (result == {'product_generated_most_revenue': 'P3',
'average_amount_of_each_product': {'Headphones': 79.99, 'Phone Case': 29.98,  'Smartwatch': 199.99}})