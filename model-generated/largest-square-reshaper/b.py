import pandas as pd
import numpy as np


# Create a sample DataFrame
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))


# Remove negative values
df = df[df > 0]


# Calculate the largest possible square
n = int(np.sqrt(len(df)))


# Reshape the DataFrame to a square shape
df = df.iloc[:n*n].values.reshape(n, -1)


# Convert the result to a DataFrame
df = pd.DataFrame(df)


print(df)