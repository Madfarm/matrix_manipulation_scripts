import pandas as pd
import numpy as np


def autocorrelation(series):
    lags = 10
    corr_list = []
    for lag in range(1, lags + 1):
        corr = np.corrcoef(series[:-lag], series[lag:])[0, 1]
        corr_list.append(corr)


    max_corr = max(corr_list)
    max_corr_lag = np.argmax(corr_list) + 1


    return corr_list, max_corr, max_corr_lag


ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))
corr_list, max_corr, max_corr_lag = autocorrelation(ser)


print(f'Autocorrelation for the first 10 lags: {corr_list}')
print(f'Lag with the largest correlation: {max_corr_lag}')
print(f'Largest correlation: {max_corr}')