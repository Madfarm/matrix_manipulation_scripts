import pandas as pd
import numpy as np


# Create a DataFrame
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})


# Find the positions where values of two columns match
matches = df['fruit1'] == df['fruit2']


# Print the positions
for i, match in enumerate(matches):
    if match:
        print(f"Match found at position: {i}")