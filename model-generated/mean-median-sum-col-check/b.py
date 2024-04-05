import pandas as pd
import numpy as np


def calculate_stats(data):
    df = pd.DataFrame(data)
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            mean = df[col].mean()
            median = df[col].median()
            std = df[col].std()
            return {'mean': mean, 'median': median, 'std': std}
    return None


data = {'name': ['abby', 'jim', 'terry'],
'breed': ['shorthair', 'tabby', 'orang'],
'age': [2,1,2]}


print(calculate_stats(data))