import nltk
from nltk.corpus import wordnet

def categorize_words(word):
    categorized_words = []
    synsets = wordnet.synsets(word)
    for synset in synsets:
        categorized_word = {
            'word': word,
            'part_of_speech': synset.pos(),
            'definition': synset.definition()
        }
        categorized_words.append(categorized_word)
    return categorized_words

print(categorize_words("accomplish"))