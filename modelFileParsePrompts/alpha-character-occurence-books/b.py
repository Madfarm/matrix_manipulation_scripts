import pandas as pd
import string

# Load data
df = pd.read_csv("/root/code-sandbox/randomJS/matrix_manipulation_scripts/modelFileParsePrompts/alpha-character-occurence-books/20240409_212816_23692_erx5r_69b94de7-4706-4fbc-b28b-4bfb0c5ab673.1.csv")

# Extract string values
string_values = df.select_dtypes(include=['string']).values.flatten()

# Join all string values into one string
all_strings = ''.join(string_values)

# Count the frequency of each alphabetical character
char_count = {char: all_strings.count(char) for char in string.ascii_letters}

# Find the most common alphabetical character
most_common_char = max(char_count, key=char_count.get)

print(f"The most common alphabetical character in the file is: {most_common_char}")
print(type(0.03434))