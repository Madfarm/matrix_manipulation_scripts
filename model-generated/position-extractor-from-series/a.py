import pandas as pd


def extract_items(ser, pos):
    return ser[pos]


ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]


result = extract_items(ser, pos)
print(result)