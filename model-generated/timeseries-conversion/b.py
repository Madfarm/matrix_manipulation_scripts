import pandas as pd


# Define the series
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])


# Convert the series to datetime
ser_dt = pd.to_datetime(ser)


print(ser_dt)