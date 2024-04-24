import decimal
from decimal import Decimal, getcontext
import random


# Set the precision to 6 decimals
getcontext().prec = 6


def calculate_mode(data):
    # Create a dictionary to store the frequency of each number
    freq = {}
    for num in data:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1


    # Find the number with the highest frequency
    max_freq = max(freq.values())
    modes = [num for num, freq in freq.items() if freq == max_freq]


    return modes


def calculate_median(data):
    n = len(data)
    s = sorted(data)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None


def calculate_std_deviation(data, mean):
    return (sum((x-mean)**2 for x in data)/len(data)).sqrt()


def main():
    # Generate a list of 1000 random decimal numbers between 0 and 100
    data = [Decimal(random.uniform(0, 100)) for _ in range(1000)]


    # Calculate the mean, mode, standard deviation, and median
    mean = sum(data) / len(data)
    mode = calculate_mode(data)
    std_deviation = calculate_std_deviation(data, mean)
    median = calculate_median(data)


    # Assert that all data points are to 6 decimals
    for num in data:
        assert num.as_tuple().exponent >= -6


    # Print the calculations
    print(f"Mean: {mean}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_deviation}")
    print(f"Median: {median}")


if __name__ == "__main__":
    main()