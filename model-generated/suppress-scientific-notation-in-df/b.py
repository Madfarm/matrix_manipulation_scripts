import pandas as pd
import numpy as np


# Create a DataFrame
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])


# Suppress scientific notation and display 4 digits after the decimal
pd.options.display.float_format = '{:.4f}'.format


# Print the DataFrame
print(df)