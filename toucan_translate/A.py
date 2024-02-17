def toucan_transcribe(text):
    # Create a dictionary to map consonants to "squawk" sounds
    consonant_map = {
        'b': 'squawk-buh',
        'c': 'squawk-kah',
        'd': 'squawk-dah',
        'f': 'squawk-fuh',
        'g': 'squawk-gah',
        'h': 'squawk-hah',
        'j': 'squawk-jah',
        'k': 'squawk-kah',
        'l': 'squawk-lah',
        'm': 'squawk-mah',
        'n': 'squawk-nah',
        'p': 'squawk-pah',
        'q': 'squawk-qah',
        'r': 'squawk-rah',
        's': 'squawk-sah',
        't': 'squawk-tah',
        'v': 'squawk-vah',
        'w': 'squawk-wah',
        'x': 'squawk-xah',
        'y': 'squawk-yah',
        'z': 'squawk-zah'
    }

    # Create a dictionary to map vowels to "trill" sounds
    vowel_map = {
        'a': 'trill-ah',
        'e': 'trill-eh',
        'i': 'trill-ih',
        'o': 'trill-oh',
        'u': 'trill-oo'
    }

    # Initialize an empty string to build the bird language output
    output = ''

    # Iterate through each character in the input text
    for char in text:
        # If the character is a consonant, replace it with the corresponding "squawk" sound
        if char in consonant_map:
            output += consonant_map[char]
        # If the character is a vowel, replace it with the corresponding "trill" sound
        elif char in vowel_map:
            output += vowel_map[char]
        # If the character is a space, number, or punctuation, keep it as-is
        else:
            output += char

    return output

# Test the function with some example input text
text = "Hello, world! This is a test message."
bird_language = toucan_transcribe(text)
print(bird_language)