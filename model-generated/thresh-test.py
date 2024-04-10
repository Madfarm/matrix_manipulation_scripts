import pandas as pd


def common_values(ser1, ser2):
    return pd.Series(list(set(ser1) & set(ser2)))


ser1 = pd.Series([1,22,3,41,5])
ser2 = pd.Series([1,2,3,4,95])


print(common_values(ser1, ser2))