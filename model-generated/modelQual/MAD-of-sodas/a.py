import pandas as pd
import numpy as np

# Create a DataFrame from the table
df = pd.DataFrame({
    'Brand': ['Coca-Cola', 'Pepsi', 'Mountain Dew', 'Dr Pepper'],
    'Parent Company': ['Coca-Cola Co.', 'PepsiCo', 'PepsiCo', 'Keurig Dr Pepper'],
    'Jan': [200, 180, 90, 80],
    'Feb': [190, 170, 85, 75],
    'Mar': [210, 190, 95, 85],
    'Apr': [220, 200, 100, 90],
    'May': [230, 210, 105, 95],
    'Jun': [240, 220, 110, 100],
    'Jul': [250, 230, 115, 105],
    'Aug': [240, 220, 110, 100],
    'Sep': [230, 210, 105, 95],
    'Oct': [220, 200, 100, 90],
    'Nov': [210, 190, 95, 85],
    'Dec': [200, 180, 90, 80]
})

# Calculate the mean absolute deviation for each soda
df['MAD'] = df.iloc[:, 2:].apply(lambda x: np.mean(np.abs(x - x.mean())), axis=1)

# Find the soda with the highest mean absolute deviation
max_mad_soda = df.loc[df['MAD'].idxmax()]['Brand']

print(df[["MAD", "Brand"]])
print(f"The soda with the highest mean absolute deviation is {max_mad_soda}.")
