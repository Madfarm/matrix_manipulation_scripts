def analyze_text(text):
    text = text.lower()  # convert text to lowercase
    text = ''.join(filter(str.isalpha, text))  # remove non-alphabetical characters
    char_dict = {char: text.count(char) for char in set(text)}  # count occurrence of each character
    char_dict['min_char'] = min(char_dict, key=char_dict.get)  # get character with minimum occurrence
    char_dict['max_char'] = max(char_dict, key=char_dict.get)  # get character with maximum occurrence
    char_dict['avg_occurrences'] = sum(char_dict.values()) / len(char_dict)  # calculate average occurrence
    char_dict['median_occurrences'] = sorted(char_dict.values())[len(char_dict) // 2]  # calculate median occurrence
    return char_dict

text = "The shape of the letters on my father's, gave me an odd idea that he was a square, stout, dark man, with curly black hair. From the character and turn of the inscription, 'Also Georgiana Wife of the Above,' I drew a childish conclusion that my mother was freckled and sickly."
print(analyze_text(text))