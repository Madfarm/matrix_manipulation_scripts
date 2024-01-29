def add_ner_and_relations(words, ners):
    """
    Adds NER information and relations to a list of words.

    Args:
        words: A list of dictionaries, where each dictionary represents a word
               with the following keys: 'id', 'text'.
        ners: A list of dictionaries, where each dictionary represents a named
              entity recognition (NER) tag with the following keys: 'id', 
              'wordId', 'nerType', 'related_nerIds'.

    Returns:
        A new list of word dictionaries with the added keys: 'nerType' and 'relations'.
    """

    # Build a lookup for word IDs
    word_lookup = {word['id']: word for word in words}

    # Process NERs and add information to words
    for ner in ners:
        word_id = ner['wordId']
        if word_id in word_lookup:
            word_lookup[word_id]['nerType'] = ner['nerType']

            # Convert related NER IDs to word IDs
            word_relations = [word_lookup[related_id]['id'] 
                              for related_id in ner['related_nerIds'] 
                              if related_id in word_lookup]
            word_lookup[word_id]['relations'] = word_relations

    # Add default values for words without NER tags
    for word in words:
        if 'nerType' not in word:
            word['nerType'] = 'other'
            word['relations'] = []

    return words


words = [
    {'id': 'w1', 'text': 'Paris'},
    {'id': 'w2', 'text': 'is'},
    {'id': 'w3', 'text': 'beautiful'}
]
ners = [
    {'id': 'n1', 'wordId': 'w1', 'nerType': 'LOCATION', 'related_nerIds': []}
]

enriched_words = add_ner_and_relations(words, ners)
print(enriched_words)