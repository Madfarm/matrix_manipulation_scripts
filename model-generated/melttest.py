import pandas as pd


def melt_df(df):
    return pd.melt(df)


df = pd.DataFrame({'w': [1, 2], 'x': [5, 6], 'y': [9, 10], 'z': [18,20]})
print(melt_df(df))