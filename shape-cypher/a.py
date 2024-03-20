def decode_note(note, key):
    # Create a dictionary to store the mapping of symbols to letters
    symbol_to_letter = {}
    for i in range(len(key)):
        symbol_to_letter[key[i]] = chr(i + 65)  # Convert index to uppercase letter

    # Create a dictionary to store the mapping of symbols to special characters
    symbol_to_special = {'triangle': '!', 'square': '@', 'circle': '#', 'diamond': '$'}

    # Initialize an empty string to store the decoded message
    decoded_message = ''

    # Iterate over the symbols in the note
    i = 0
    while i < len(note):
        symbol = note[i]

        # If the symbol is repeated consecutively, append the special character to the decoded message
        if i < len(note) - 1 and note[i] == note[i + 1]:
            decoded_message += symbol_to_special[symbol]
            i += 2  # Skip the next symbol
        else:
            decoded_message += symbol_to_letter[symbol]
            i += 1

    return decoded_message

# Test the function
note = ['triangle', 'square', 'square', 'square', 'circle', 'circle', 'triangle', 'triangle', 'square', 'square', 'square']
key = ['triangle', 'square', 'circle', 'diamond']
print(decode_note(note, key))  # Output: "A@B#!@B"