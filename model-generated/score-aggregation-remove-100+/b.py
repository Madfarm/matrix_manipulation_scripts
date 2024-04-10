import pandas as pd


def process_array(arr):
    # Negate all elements above 100
    arr = [-x if x > 100 else x for x in arr]


    # Convert the array to a series
    series = pd.Series(arr)


    # Calculate the mean, median, and standard deviation
    mean = series.mean()
    median = series.median()
    std_dev = series.std()


    # Create a dictionary with the results
    results = {
        'series': series,
        'mean': mean,
        'median': median,
        'standard_deviation': std_dev
    }


    return results


# Test the function with the provided input
arr = [45,43,67,72,81,80,112,92,97,98,127,94,91,35,76,62,183,79,81,199,151]
results = process_array(arr)


# Print the results
print(results)