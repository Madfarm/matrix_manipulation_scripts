import pandas as pd
import numpy as np


def aggregate_column(df, column):
    aggs = ['mean', 'min', 'max', 'std']
    return {agg: df[column].agg(agg) for agg in aggs}


df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


print(aggregate_column(df, 'Salary'))