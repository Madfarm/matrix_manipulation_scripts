def character_occurrence(text):
    text = text.lower()
    # Create a dictionary to store the occurrence of each character
    char_occurrence = {}
    
    # Loop through each character in the text
    for char in text:
        # If the character is alphabetical, add it to the dictionary
        if char.isalpha():
            if char in char_occurrence:
                char_occurrence[char] += 1
            else:
                char_occurrence[char] = 1
                
    # Calculate the average and median number of occurrences
    average_occurrence = sum(char_occurrence.values()) / len(char_occurrence)
    median_occurrence = sorted(char_occurrence.values())[len(char_occurrence) // 2]
    
    # Find the character that occurred the least and the most
    least_occurrence = min(char_occurrence, key=char_occurrence.get)
    most_occurrence = max(char_occurrence, key=char_occurrence.get)
    
    # Add the additional information to the dictionary
    char_occurrence['least_occurrence'] = least_occurrence
    char_occurrence['most_occurrence'] = most_occurrence
    char_occurrence['average_occurrence'] = average_occurrence
    char_occurrence['median_occurrence'] = median_occurrence
    
    return char_occurrence

text = "The shape of the letters on my father's, gave me an odd idea that he was a square, stout, dark man, with curly black hair. From the character and turn of the inscription, 'Also Georgiana Wife of the Above,' I drew a childish conclusion that my mother was freckled and sickly."

print(character_occurrence(text))