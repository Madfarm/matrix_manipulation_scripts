import pandas as pd


def transform_data(df):
    # Remove columns containing nan values
    df = df.dropna(axis=1)


    # Sort columns alphabetically, except 'order_no'
    cols = sorted([col for col in df.columns if col != 'ord_no'])
    df = df[['ord_no'] + cols]


    # Truncate all values to two decimals
    df = df.round(2)


    return df


orders_data = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5123,270.65111,65.26,110.58843,948.5,2400.6,5760.23,1983.413,2480.4,250.4665, 75.229,3045.679],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})

transformed_data = transform_data(orders_data)

assert transformed_data.isnull().sum().sum() == 0, "Input data contains nan values"
assert transformed_data['ord_no'].equals(pd.Series([70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013])), "Order numbers are not correct"
assert transformed_data.columns.tolist() == ['ord_no', 'customer_id', 'ord_date', 'purch_amt', 'salesman_id'], "Columns are not in the correct order"


print(transformed_data)