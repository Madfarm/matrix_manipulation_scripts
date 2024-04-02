import pandas as pd


# Define a function to convert date-strings to datetime objects
def convert_to_datetime(date_string):
    try:
        return pd.to_datetime(date_string)
    except ValueError:
        return pd.NaT


# Create a sample series
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])


# Convert the series to datetime
ser_dt = ser.apply(convert_to_datetime)


print(ser_dt)