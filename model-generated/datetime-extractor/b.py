import pandas as pd
from datetime import datetime


def extract_date_info(date_str):
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    return dt.day, dt.isocalendar()[1], dt.timetuple().tm_yday, dt.strftime('%A')


def extract_date_info_series(date_series):
    return date_series.apply(lambda x: extract_date_info(x))


ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
ser = pd.to_datetime(ser)


date_info = extract_date_info_series(ser)


print("Date:", date_info.apply(lambda x: x[0]))
print("Week number:", date_info.apply(lambda x: x[1]))
print("Day num of year:", date_info.apply(lambda x: x[2]))
print("Day of week:", date_info.apply(lambda x: x[3]))