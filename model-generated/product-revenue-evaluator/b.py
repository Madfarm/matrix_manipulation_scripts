import pandas as pd


def calculate_revenue(df):
    # Calculate the total revenue for each product
    df['Revenue'] = df['Price'] * df['Quantity']


    # Group by 'Product ID' and sum up the revenues to get the total revenue per product
    product_revenues = df.groupby('Product ID')['Revenue'].sum()


    # Find the product with the most revenue
    max_revenue_product_id = product_revenues.idxmax()
    max_revenue_amount = product_revenues.max()


    # Calculate the average amount of revenue generated from each product
    avg_revenue_per_product = product_revenues.mean()


    return {
        "product": max_revenue_product_id,
        "revenue": max_revenue_amount,
        "avg_revenue": avg_revenue_per_product
    }


# Test data
data = [
    {'Order ID': 100, 'Customer ID': 123, 'Product ID': 'P1', 'Product Name': 'Phone Case', 'Order Date': '2024-01-10', 'Price': 14.99, 'Quantity': 2},
    {'Order ID': 101, 'Customer ID': 123, 'Product ID': 'P2', 'Product Name': 'Headphones', 'Order Date': '2024-01-10', 'Price': 79.99, 'Quantity': 1},
    {'Order ID': 102, 'Customer ID': 456, 'Product ID': 'P3', 'Product Name': 'Smartwatch', 'Order Date': '2024-01-15', 'Price': 199.99, 'Quantity': 1},
    {'Order ID': 103, 'Customer ID': 123, 'Product ID': 'P2', 'Product Name': 'Headphones', 'Order Date': '2024-02-01', 'Price': 79.99, 'Quantity': 1},
    {'Order ID': 104, 'Customer ID': 789, 'Product ID': 'P1', 'Product Name': 'Phone Case', 'Order Date': '2024-02-05', 'Quantity': 1},
]


df = pd.DataFrame(data)


result = calculate_revenue(df)
print(result)