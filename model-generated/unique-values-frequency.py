import pandas as pd
import numpy as np


# Create a DataFrame with random integers
df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))


# Get the frequency of unique values in the DataFrame
freq = df.stack().value_counts()


print(freq)