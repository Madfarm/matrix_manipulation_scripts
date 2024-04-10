import pandas as pd
import numpy as np


# Create the dataframe
data = {'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu', 'Ash', 'Ash', 'Jiametryc', 'Eshanta', 'Eshanta', 'Ash', 'Jiametryc', 'Seth', 'Eshanta', 'Ash', 'Jiametryc', 'Wallu', 'Eshanta', 'Wallu', 'Wallu', 'Ash', 'Seth', 'Seth', 'Seth', 'Wallu', 'Seth'],
        'GPA': [2.4, 3.8, np.nan, np.nan, 2.1, 2.830082, 2.968065, 3.145037, 2.332947, 3.200439, 3.084441, 3.769235, 2.277073, 3.430214, 2.143005, 2.575336, 2.972720, 3.374090, 2.553177, 2.471817, 3.273595, 2.345142, 3.799689, 2.860008, 3.283964, 2.177317],
        'Age': [30, 56, 81, np.nan, 21, 69.333371, 21.249461, 22.088721, 30.479066, 46.732833, 55.743946, 75.639865, 68.561340, 63.493539, 28.080501, 52.415456, 52.317297, 53.655957, 77.278997, 36.175471, 44.829222, 67.945110, 61.214862, 50.640961, 65.620693, 52.348202],
        'Salary': [np.nan, 80000, 41000, 33000, 20900, 55166.023307, 68923.175160, 23659.193876, 57251.114153, 45178.500416, 23875.428034, 50839.129276, 42029.516060, 51166.216193, 41632.700859, 45941.567499, 36705.947460, 77655.282044, 60665.962657, 47036.495174, 77391.982265, 58091.640476, 28325.808124, 22195.411298, 54316.134729, 44791.272609]}


df = pd.DataFrame(data)


# Group by 'Name' and calculate the median for each numeric column
medians = df.groupby('Name').median()


# Merge the medians with the original dataframe
df = df.merge(medians, on='Name', suffixes=('', '_median'))


# Replace the numeric columns with the median values
df[['GPA', 'Age', 'Salary']] = df[['GPA_median', 'Age_median', 'Salary_median']]


# Drop the median columns
df = df.drop(['GPA_median', 'Age_median', 'Salary_median'], axis=1)


# Drop duplicate rows
df = df.drop_duplicates(subset='Name')


print(df)