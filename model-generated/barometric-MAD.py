import numpy as np

def median_absolute_deviation(data):
    median_value = np.median(data)
    abs_diffs = np.abs(data - median_value)
    mad = np.median(abs_diffs)
    return mad


meso = (0.0046 + 0.8) / 2
trop = (223 + 1013) / 2
strat = (1.1 + 79) / 2

barometric_pressure_data = np.array([meso, strat, trop])  


mad = median_absolute_deviation(barometric_pressure_data)
print(mad)
