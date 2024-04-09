import pandas as pd
import numpy as np


def generate_heatmap(df):
    # Create a pivot table to reshape the data
    heatmap = df.pivot(index='beta', columns='alpha', values='accuracy')
    return heatmap


# Create a DataFrame from the input data
df = pd.DataFrame({
    'alpha': [0, 0, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.7, 0.7, 0.7, 0.7, 1, 1, 1, 1],
    'beta': [0, 0.3, 0.7, 1, 0, 0.3, 0.7, 1, 0, 0.3, 0.7, 1, 0, 0.3, 0.7, 1],
    'accuracy': [0.112186, 0.513274, 0.722594, 0.720604, 0.319968, 0.711226, 0.946665, 0.93472, 0.330959, 0.706973, 0.934994, 0.910779, 0.108678, 0.510815, 0.742989, 0.703605]
})


# Generate the heatmap
heatmap = generate_heatmap(df)


# Print the heatmap
print(heatmap)