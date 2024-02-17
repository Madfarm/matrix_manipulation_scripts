def toucan_transcribe(text):
    # Define the toucan sounds for consonants and vowels
    consonant_map = {
        "p": "squawk",
        "t": "squawk",
        "k": "squawk",
        "b": "squawk",
        "d": "squawk",
        "g": "squawk",
        "f": "f squawk",
        "v": "v squawk",
        "s": "s squawk",
        "h": "h squawk",
        "j": "j squawk",
        "l": "l squawk",
        "m": "m squawk",
        "n": "n squawk",
        "r": "r squawk",
        "w": "w squawk",
        "x": "x squawk",
        "y": "y squawk",
        "z": "z squawk"
    }
    vowel_map = {"a": "trill", "e": "trill", "i": "trill", "o": "trill", "u": "trill"}

    # Define a function to replace consonants and vowels
    def replace_sound(char):
        if char in consonant_map:
            return consonant_map[char]
        elif char in vowel_map:
            return vowel_map[char]
        else:
            return char  # Keep space, numbers, and punctuation unchanged

    # Apply the replacement function to each character in the input text
    output = "".join(map(replace_sound, text))

    return output

# Test the function
input_text = "Hello, world! 😊"
output_text = toucan_transcribe(input_text)
print(output_text)