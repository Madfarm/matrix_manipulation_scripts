import pandas as pd
import numpy as np
from scipy import stats


def generate_sample_data():
    # Generate a sample dataset with random values
    data = pd.DataFrame(np.random.randn(100, 1), columns=['Values'])
    return data


def detect_outliers(data):
    # Calculate Z-scores for the data
    z_scores = np.abs(stats.zscore(data['Values']))


    # Identify outliers as data points whose absolute Z-score is greater than 3
    outliers = data[z_scores > 3]


    # Return a list of indices corresponding to the outliers found in the dataset
    return outliers.index.tolist()


# Generate sample data
data = generate_sample_data()


# Detect outliers
outliers = detect_outliers(data)


# Print outliers
print(outliers)


# Assertions to validate the calculations
assert len(outliers) >= 0, "Outliers should be a list"
assert all(isinstance(outlier, int) for outlier in outliers), "Outliers should be integers"


# Example assertion if you know the expected outliers
expected_outliers = []  # Replace with expected outliers
assert outliers == expected_outliers, "Outliers do not match the expected values"