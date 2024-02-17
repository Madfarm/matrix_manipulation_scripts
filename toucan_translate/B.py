def toucan_transcribe(text):
    # Define the toucan sounds for consonants and vowels as lists
    consonant_map = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vowel_map = ["a", "e", "i", "o", "u"]

    # Define a function to replace consonants and vowels
    def replace_sound(char):
        char = char.casefold()  # Convert to case-insensitive equivalent
        if char in consonant_map:
            return "squawk"
        elif char in vowel_map:
            return "trill"
        else:
            return char  # Keep space, numbers, and punctuation unchanged

    # Apply the replacement function to each character in the input text
    output = "".join(map(replace_sound, text))

    return output

# Test the function
input_text = "Hello, World! 😊"
output_text = toucan_transcribe(input_text)
print(output_text)