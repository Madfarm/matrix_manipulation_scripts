import pandas as pd
import numpy as np


# Create a DataFrame
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))


# Find rows where the sum of the row is greater than 100
df_filtered = df[df.apply(lambda x: x.sum(), axis=1) > 100]


# Select the last two rows
last_two_rows = df_filtered.tail(2)


print(last_two_rows)