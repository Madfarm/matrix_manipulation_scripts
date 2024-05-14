import pandas as pd

def calculate_customer_retention(data):
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Convert the 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Calculate the number of unique customers for each month
    num_customers = df.groupby(df['date'].dt.to_period('M'))['customer_id'].nunique()

    # Get the most recent month
    most_recent_month = num_customers.index[-1]

    # Get the second most recent month
    second_most_recent_month = num_customers.index[-2]

    # Get the unique customers in the most recent month
    most_recent_month_customers = df[df['date'].dt.to_period('M') == most_recent_month]['customer_id'].unique()

    # Get the unique customers in the second most recent month
    second_most_recent_month_customers = df[df['date'].dt.to_period('M') == second_most_recent_month]['customer_id'].unique()

    # Calculate the number of retained customers
    retained_customers = len(set(most_recent_month_customers) & set(second_most_recent_month_customers))

    # Calculate customer retention for the most recent month
    customer_retention = retained_customers / len(second_most_recent_month_customers)

    return customer_retention

data = {
    'date': ['2019-08-01', '2019-08-05', '2019-09-01', '2019-09-07'],
    'customer_id': [1, 2, 1, 3],
    'order_num': [1, 2, 3, 4],
    'order_amount_dollars': [30, 40, 30, 50]
}

assert round(calculate_customer_retention(data), 2) == 0.5