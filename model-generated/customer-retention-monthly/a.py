import pandas as pd


def calculate_customer_retention(data):
    # Convert the data into a dataframe
    df = pd.DataFrame(data)


    # Convert the 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])


    # Set the 'date' column as the index
    df.set_index('date', inplace=True)


    # Resample the dataframe by month and count the number of unique customers
    num_customers = df['customer_id'].resample('M').nunique()


    # Calculate customer retention
    customer_retention = num_customers[-1] / num_customers[-2]


    return customer_retention


# Test the function
data = {
    'date': ['2019-08-01', '2019-08-05', '2019-09-01', '2019-09-07'],
    'customer_id': [1, 2, 1, 3],
    'order_num': [1, 2, 3, 4],
    'order_amount_dollars': [30, 40, 30, 50]
}


print(calculate_customer_retention(data))