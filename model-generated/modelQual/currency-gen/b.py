import random
import string
from decimal import Decimal
import statistics

def generate_currency(num_currencies):
    currencies = {}
    names = set()
    
    while len(names) < num_currencies:
        name = ''.join(random.choices(string.ascii_uppercase, k=3))
        names.add(name)
    
    for name in names:
        value = Decimal(str(random.random()))
        currencies[name] = value
    
    values = list(currencies.values())
    mean = sum(values) / len(values)
    median = statistics.median(values)
    
    return {
        'currencies': currencies,
        'mean': mean,
        'median': median
    }

num_currencies = 3
result = generate_currency(num_currencies)

# Assertions
assert all(len(name) == 3 and name.isalpha() and name.isupper() for name in result['currencies']), "Names do not follow the guidelines"
assert all(isinstance(value, Decimal) for value in result['currencies'].values()), "Values are not of Decimal type"

values = list(result['currencies'].values())
assert result['mean'] == sum(values) / len(values), "Mean is incorrect"
assert result['median'] == statistics.median(values), "Median is incorrect"

print(result)