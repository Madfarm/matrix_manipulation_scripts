def toucan_transcribe(text):
    # Define the toucan sounds for consonants and vowels
    consonant_map = {
        "p": "squawk",
        "t": "squawk",
        "k": "squawk",
        "b": "squawk",
        "d": "squawk",
        "g": "squawk",
        "f": "squawk",
        "h": "squawk",
        "j": "squawk",
        "l": "squawk",
        "m": "squawk",
        "n": "squawk",
        "r": "squawk",
        "s": "squawk",
        "v": "squawk",
        "w": "squawk",
        "x": "squawk",
        "y": "squawk",
        "z": "squawk"
    }
    vowel_map = {"a": "trill", "e": "trill", "i": "trill", "o": "trill", "u": "trill"}

    # Define a function to replace consonants and vowels
    def replace_sound(char):
        if char in consonant_map:
            return "squawk"  # Every consonant gets replaced with just "squawk"
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