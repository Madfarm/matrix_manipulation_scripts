import random
import string
from decimal import Decimal
import statistics

def generate_currency(num_currencies):
    currencies = {}
    for _ in range(num_currencies):
        name = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        while name in currencies:
            name = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        value = Decimal(str(round(random.random(), 2)))
        currencies[name] = value
    
    # Calculate mean and median
    values = list(currencies.values())
    mean_value = sum(values) / len(values)
    median_value = statistics.median(values)

    return {
        'currencies': currencies,
        'mean': mean_value,
        'median': median_value
    }

num_currencies = 3
result = generate_currency(num_currencies)

# Assertions
assert all(len(name) == 3 and name.isalpha() and name.isupper() for name in result['currencies'].keys()), "Currency names do not follow the guidelines"
assert all(isinstance(value, Decimal) for value in result['currencies'].values()), "Values are not of Decimal type"
assert sum(result['currencies'].values()) / len(result['currencies']) == result['mean'], "Mean is incorrect"
assert statistics.median(list(result['currencies'].values())) == result['median'], "Median is incorrect"

print(result)