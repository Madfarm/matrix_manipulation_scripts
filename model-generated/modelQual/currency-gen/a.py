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
        value = Decimal(str(random.random()))
        currencies[name] = value
    
    mean_value = sum(currencies.values()) / len(currencies)
    median_value = statistics.median(currencies.values())
    
    return {
        'currencies': currencies,
        'mean': mean_value,
        'median': median_value
    }

num_currencies = 3
result = generate_currency(num_currencies)

# Assertions
for name in result['currencies']:
    assert len(name) == 3, "Name length is not 3"
    assert name.isalpha(), "Name contains non-alphabetical characters"
    assert name.isupper(), "Name is not uppercase"
    assert isinstance(result['currencies'][name], Decimal), "Value is not a Decimal"

assert result['mean'] == sum(result['currencies'].values()) / len(result['currencies']), "Mean is incorrect"
assert result['median'] == statistics.median(result['currencies'].values()), "Median is incorrect"
