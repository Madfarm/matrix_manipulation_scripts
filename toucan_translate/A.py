def toucan_transcribe(text):
    # Define the toucan sounds for consonants and vowels as lists
    consonant_map = ["squawk"] * 26
    vowel_map = ["trill"] * 5

    # Define a function to replace consonants and vowels
    def replace_sound(char):
        if char.islower():
            char = char.upper()
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