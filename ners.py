def enrich_words_with_ners(words, ners):
    # Step 1: Create a word dictionary for quick access by word ID.
    word_dict = {word['id']: word for word in words}
    
    # Step 2: Create a mapping from word IDs to their NERs.
    ner_mapping = {}
    for ner in ners:
        word_id = ner['wordId']
        ner_type = ner['nerType']
        related_ners = ner['related_nerIds']
        ner_mapping[word_id] = {
            'nerType': ner_type,
            'related_wordIds': [ner_mapping[rel_ner_id]['wordId'] for rel_ner_id in related_ners if rel_ner_id in ner_mapping]
        }
    
    # Step 3: Enrich words with NER information.
    enriched_words = []
    for word in words:
        word_id = word['id']
        if word_id in ner_mapping:
            ner_info = ner_mapping[word_id]
            word['nerType'] = ner_info['nerType']
            word['relations'] = ner_info['related_wordIds']
        else:
            word['nerType'] = 'other'
            word['relations'] = []
        enriched_words.append(word)
    
    return enriched_words

# Example usage:
words = [
    {'id': 'w1', 'text': 'Paris'},
    {'id': 'w2', 'text': 'is'},
    {'id': 'w3', 'text': 'beautiful'}
]
ners = [
    {'id': 'n1', 'wordId': 'w1', 'nerType': 'LOCATION', 'related_nerIds': []}
]

enriched_words = enrich_words_with_ners(words, ners)
print(enriched_words)