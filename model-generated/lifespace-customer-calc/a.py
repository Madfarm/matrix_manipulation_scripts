import pandas as pd


def calculate_customer_lifespan(df):
    # Calculate the duration between the first and last order for each customer
    customer_durations = df.groupby('customer_id')['date'].apply(lambda x: x.max() - x.min())


    # Calculate the average customer lifespan
    average_lifespan = customer_durations.mean()


    return average_lifespan


# Create a DataFrame with the provided data
data = {
    'date': ['2019-08-01', '2019-08-05', '2019-09-01'],
    'customer_id': [1, 2, 1],
    'order_num': [1, 2, 3],
    'order_amount_dollars': [30, 40, 30]
}
df = pd.DataFrame(data)


# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])


# Calculate and print the average customer lifespan
average_lifespan = calculate_customer_lifespan(df)
print(average_lifespan)