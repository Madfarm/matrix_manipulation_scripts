import pandas as pd


def filter_df(df, conditions):
    return df[conditions]


df = pd.DataFrame({'name': ['Jeff', 'Esha', 'Jia'], 
                   'age': [30, 56, 8],
                   'city': ['New York', 'Atlanta', 'Shanghai']})


conditions = (df['age'] >= 21) & (df['age'] <= 40) & ((df['city'] == 'New York') | (df['city'] == 'Tokyo'))


print(filter_df(df, conditions))