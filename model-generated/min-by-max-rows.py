import pandas as pd
import numpy as np


def min_by_max(df):
    return df.apply(lambda x: x.min() / x.max(), axis=1)


df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
print(min_by_max(df))