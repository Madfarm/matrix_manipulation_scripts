import numpy as np
from fractions import Fraction


def mean_as_fraction(data):
    assert isinstance(data, list), "Input must be a list."
    assert all(isinstance(x, int) for x in data), "All elements in the list must be integers."
    mean = np.mean(data)
    fraction = Fraction(mean).limit_denominator()
    assert isinstance(fraction, Fraction), "Output must be a Fraction."
    return fraction


data = [1, 2, 3, 4, 5]
assert mean_as_fraction(data) == 3