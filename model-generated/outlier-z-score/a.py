import pandas as pd
import random
from scipy import stats


def generate_sample_data():
    # Generate a sample dataset with random values
    data = [random.gauss(0, 1) for _ in range(100)]
    df = pd.DataFrame(data, columns=['Value'])
    return df


def detect_outliers(df):
    # Calculate Z-scores
    z_scores = stats.zscore(df['Value'])


    # Define the threshold
    threshold = 3


    # Identify outliers
    outliers = df[(abs(z_scores) > threshold)]


    return outliers.index.tolist()


# Generate sample data
df = generate_sample_data()
print(df)

# Detect outliers
outliers = detect_outliers(df)
print(outliers)