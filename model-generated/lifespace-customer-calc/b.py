import pandas as pd


def average_customer_lifespan(df):
    # Calculate the time difference between the first and last order for each customer
    df['date'] = pd.to_datetime(df['date'])
    df['customer_id'] = df['customer_id'].astype(int)
    df['order_num'] = df['order_num'].astype(int)
    df['order_amount_dollars'] = df['order_amount_dollars'].astype(float)
    df['date_diff'] = df.groupby('customer_id')['date'].transform(lambda x: x.max() - x.min())


    # Calculate the average time difference
    avg_lifespan = df['date_diff'].mean()


    return avg_lifespan


# Create a DataFrame
df = pd.DataFrame({
    'date': ['2019-08-01', '2019-08-05', '2019-09-01'],
    'customer_id': [1, 2, 1],
    'order_num': [1, 2, 3],
    'order_amount_dollars': [30, 40, 30]
})


# Calculate the average customer lifespan
avg_lifespan = average_customer_lifespan(df)


print(f'The average customer lifespan is {avg_lifespan.days} days.')