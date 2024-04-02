import pandas as pd


def get_peaks(ser):
    peaks = []
    for i in range(1, len(ser) - 1):
        if ser[i] > ser[i-1] and ser[i] > ser[i+1]:
            peaks.append(i)
    return peaks


# Test the function
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])
print(get_peaks(ser))  # Output: [1, 5, 7]