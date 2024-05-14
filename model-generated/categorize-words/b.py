import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet as wn

def get_wordnet_pos(treebank_tag):
    """Converts treebank tags to wordnet tags."""
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None

def categorize_words(sentence):
    categorized = []
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)
    
    for word, tag in tagged_tokens:
        wn_tag = get_wordnet_pos(tag)
        if wn_tag is not None:
            definitions = wn.synsets(word, pos=wn_tag)
            if definitions:
                definition = definitions[0].definition()
                categorized.append({'word': word, 'part_of_speech': wn_tag, 'definition': definition})
    return categorized

print(categorize_words("accomplish"))