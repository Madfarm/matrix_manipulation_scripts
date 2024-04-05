import statistics


def calculate_stats(data):
    for key, values in data.items():
        if all(isinstance(value, (int, float)) for value in values):
            mean = statistics.mean(values)
            median = statistics.median(values)
            std_dev = statistics.stdev(values)
            return {
                "mean": mean,
                "median": median,
                "standard deviation": std_dev
            }
    return {}

data = {'name': ['abby', 'jim', 'terry'],
        'breed': ['shorthair', 'tabby', 'orang'],
        'age': [2,1,2]}

print(calculate_stats(data))