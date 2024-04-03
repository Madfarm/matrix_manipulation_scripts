import pandas as pd
import numpy as np


# Creating a dataframe with two columns 'fruit1' and 'fruit2'
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})


# Finding the positions where 'fruit1' and 'fruit2' match
positions = df.index[df['fruit1'] == df['fruit2']]


# Printing the positions
print(positions)