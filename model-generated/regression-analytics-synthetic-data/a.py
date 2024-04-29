import pandas as pd
import numpy as np
from scipy import stats

def generate_synthetic_data(num_samples, num_features, noise_level):
    # Generate random features from a normal distribution
    features = np.random.normal(0, 1, (num_samples, num_features))
    
    # Generate random coefficients for the linear combination
    coefficients = np.random.normal(0, 1, num_features)
    
    # Generate the target variable as a linear combination of the features plus random noise
    target = np.dot(features, coefficients) + np.random.normal(0, noise_level, num_samples)
    
    # Create a DataFrame containing the generated data
    data = pd.DataFrame(features, columns=[f'feature_{i}' for i in range(num_features)])
    data['target'] = target
    
    return data

# Demonstration of the function
np.random.seed(0)  # For reproducibility
data = generate_synthetic_data(100, 5, 0.1)
print(data.head())