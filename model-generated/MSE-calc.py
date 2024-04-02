import pandas as pd
import numpy as np


def calculate_mse(truth, pred):
    return ((truth - pred) ** 2).mean()


truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)


print(calculate_mse(truth, pred))