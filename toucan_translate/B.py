def toucan_transcribe(text):
    # Define the toucan sounds for consonants and vowels
    consonant_map = {"p": "psquawk", "t": "tsquawk", "k": "ksquawk", "b": "bsquawk", "d": "dsquawk", "g": "gsquawk"}
    vowel_map = {"a": "atrill", "e": "etrill", "i": "itrill", "o": "otrill", "u": "utrill"}

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
