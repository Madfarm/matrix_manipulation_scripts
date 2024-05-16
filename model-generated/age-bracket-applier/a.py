import pandas as pd
import numpy as np


df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


bins = [0, 10, 19, 31, 50, 65, 80, 120]
labels = ['0-10', '11-18', '19-30', '31-50', '51-65', '66-80', '81-120']
df['Age_Bracket'] = pd.cut(df['Age'], bins, labels=labels, right=False)
assert df['Age_Bracket'].tolist() == ["19-30", "51-65", "81-120", np.nan, "19-30"]