import pandas as pd
import numpy as np
from scipy import stats

def clean_normalize_detect_outliers(sensor_data):
    # Clean the data by removing all nan values
    cleaned_data = sensor_data.apply(lambda x: [i for i in x if not np.isnan(i)])

    # Normalize the data
    normalized_data = cleaned_data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

    # Find potential outliers using z-score
    z_scores = normalized_data.apply(stats.zscore)
    potential_outliers = z_scores.apply(lambda x: np.abs(x) > 2)

    return normalized_data, potential_outliers

sensor_data = pd.Series([
    [0.1, 0.2, np.nan, 0.4],
    [0.5, 0.6, 0.7, 0.8],
    [0.9, np.nan, 1.1, 1.2],
    [1.3, 1.4, 1.5, 1.6]
])

normalized_data, potential_outliers = clean_normalize_detect_outliers(sensor_data)

# Validate the results
assert len(normalized_data) == len(sensor_data), "Length of normalized data does not match input data"
assert all([all(np.isfinite(x)) for x in normalized_data]), "Normalized data contains non-finite values"
assert all([all(np.logical_or(x >= 0, np.isclose(x, 0))) for x in normalized_data]), "Normalized data contains negative values"
assert all([all(np.logical_or(x <= 1, np.isclose(x, 1))) for x in normalized_data]), "Normalized data contains values greater than 1"

assert len(potential_outliers) == len(sensor_data), "Length of potential outliers does not match input data"
assert all([isinstance(x, np.ndarray) for x in potential_outliers]), "Potential outliers are not numpy arrays"
assert all([x.dtype == bool for x in potential_outliers]), "Potential outliers are not boolean arrays"