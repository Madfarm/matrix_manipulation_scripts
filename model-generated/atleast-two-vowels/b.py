import pandas as pd


# Create a function to check if a word contains at least 2 vowels
def has_two_vowels(word):
    vowels = 'aeiou'
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count >= 2


# Apply the function to the series
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
result = ser[ser.apply(has_two_vowels)]


print(result)