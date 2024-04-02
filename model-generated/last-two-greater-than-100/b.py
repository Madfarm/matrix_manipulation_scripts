import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))


# Calculate the sum of each row
df['row_sum'] = df.sum(axis=1)


# Filter rows with sum greater than 100
df_filtered = df[df['row_sum'] > 100]


# Select the last two rows
last_two_rows = df_filtered.tail(2)


print(last_two_rows)