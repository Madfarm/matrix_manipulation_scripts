import pandas as pd
import numpy as np


# Create a DataFrame with random integers
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))


arr = df[df > 0].values.flatten()
arr_qualified = arr[~np.isnan(arr)]

# Step 2: find side-length of largest possible square
n = int(np.floor(arr_qualified.shape[0]**.5))

# Step 3: Take top n^2 items without changing positions
top_indexes = np.argsort(arr_qualified)[::-1]
output = np.take(arr_qualified, sorted(top_indexes[:n**2])).reshape(n, -1)

print(output)