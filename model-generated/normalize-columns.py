import pandas as pd
import numpy as np


def normalize_df(df):
    return df.apply(lambda x: (x - x.min()) / (x.max() - x.min()))


df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
print("Original DataFrame:")
print(df)
print("\nNormalized DataFrame:")
print(normalize_df(df))