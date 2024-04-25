import numpy as np
import re


def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()


    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)


    # Tokenize into words
    words = text.split()


    return words


def calculate_ngram_frequencies(words, n):
    # Initialize an empty dictionary to store n-gram frequencies
    ngram_freq = {}


    # Iterate over the list of words
    for i in range(len(words) - n + 1):
        # Extract the n-gram
        ngram = tuple(words[i:i+n])


        # Increment the frequency of the n-gram
        if ngram in ngram_freq:
            ngram_freq[ngram] += 1
        else:
            ngram_freq[ngram] = 1


    return ngram_freq


# Input text
text = """This is a sample text file for n-gram analysis. It contains a few sentences 
to demonstrate how frequently sequences of words (n-grams) appear together. 
The text discusses natural language processing and its applications. 


By analyzing n-gram frequencies, we can gain insights into the language patterns 
used in the text. This can be useful for various tasks like text classification, 
machine translation, and even language modeling for generating similar text."""


# Preprocess the text
words = preprocess_text(text)


# Calculate n-gram frequencies
ngram_freq = calculate_ngram_frequencies(words, 2)


# Print the n-gram frequencies
for ngram, freq in ngram_freq.items():
    print(f"{ngram}: {freq}")