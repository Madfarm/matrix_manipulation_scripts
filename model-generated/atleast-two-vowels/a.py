import pandas as pd


def extract_words_with_vowels(ser):
    vowels = 'aeiou'
    return [word for word in ser if sum(1 for char in word.lower() if char in vowels) >= 2]


ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
print(extract_words_with_vowels(ser))