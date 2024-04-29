import pandas as pd
import numpy as np
from scipy import stats

def generate_synthetic_data(num_samples, num_features, noise_level):
    # Generate random features from a normal distribution
    features = np.random.normal(loc=0, scale=1, size=(num_samples, num_features))
    
    # Generate random coefficients for the linear combination
    coefficients = np.random.normal(loc=0, scale=1, size=num_features)
    
    # Generate the target variable as a linear combination of the features plus random noise
    target_variable = np.dot(features, coefficients) + np.random.normal(loc=0, scale=noise_level, size=num_samples)
    
    # Create a DataFrame containing the generated data
    data = pd.DataFrame(features, columns=[f'feature_{i}' for i in range(num_features)])
    data['target'] = target_variable
    
    return data

# Demonstration of the function
data = generate_synthetic_data(num_samples=100, num_features=3, noise_level=0.1)
print(data.head())