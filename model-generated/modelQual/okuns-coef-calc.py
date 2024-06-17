import numpy as np
import pandas as pd


# Hypothetical data
data = { "Year": [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 
        "GDP_Growth": [2.5, 2.3, 2.9, 3.1, 2.7, -3.5, 5.9, 3.2, 1.3], 
        "Unemployment_Rate": [5.0, 4.8, 4.4, 4.0, 3.8, 8.1, 5.3, 4.2, 3.9] }


df = pd.DataFrame(data)

# Calculate changes
df['Delta_U'] = df['Unemployment_Rate'].diff()
df['Delta_Y'] = df['GDP_Growth'].diff()

# Drop NaN values (first row will be NaN due to differencing)
df = df.dropna()

# Independent variable (change in unemployment rate)
delta_u = df['Delta_U'].values
# Dependent variable (change in GDP growth rate)
delta_y = df['Delta_Y'].values

# Calculate means
mean_delta_u = np.mean(delta_u)
mean_delta_y = np.mean(delta_y)

# Calculate covariance and variance
cov_delta_y_u = np.mean((delta_u - mean_delta_u) * (delta_y - mean_delta_y))
var_delta_u = np.mean((delta_u - mean_delta_u) ** 2)

# Calculate Okun's coefficient (slope)
okun_coefficient = cov_delta_y_u / var_delta_u

# Calculate intercept
intercept = mean_delta_y - okun_coefficient * mean_delta_u

print(f"The Okun's Coefficient is {okun_coefficient}")