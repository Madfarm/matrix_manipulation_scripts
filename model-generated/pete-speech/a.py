def parrot_learn(phrase):
    words = phrase.split()
    words.sort(key=lambda x: (-len(x), x))  # sort by length (descending), then alphabetically
    learned_phrase = ''
    for word in words:
        if word not in learned_phrase:
            learned_phrase += word + ' '
            print(learned_phrase)

# Test the function
parrot_learn('The quick brown fox jumps over the lazy dog')