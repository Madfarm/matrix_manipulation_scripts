import numpy as np
import re
from collections import Counter


def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()


    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)


    # Tokenize into words
    words = text.split()


    return words


def calculate_ngram_frequencies(words, n):
    # Calculate n-grams
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]


    # Calculate frequencies
    frequencies = Counter(ngrams)


    return frequencies


text = """This is a sample text file for n-gram analysis. It contains a few sentences 
to demonstrate how frequently sequences of words (n-grams) appear together. 
The text discusses natural language processing and its applications. 


By analyzing n-gram frequencies, we can gain insights into the language patterns 
used in the text. This can be useful for various tasks like text classification, 
machine translation, and even language modeling for generating similar text."""


words = preprocess_text(text)

ngram_frequencies = calculate_ngram_frequencies(words, 2)


assert len(words) == 69
assert ngram_frequencies['is a'] == 1
assert ngram_frequencies['language processing'] == 1