def convert_string(s):
    return ' '.join(word[0].lower() + word[1:].upper() for word in s.split())

s = "The quick brown fox jumps over the lazy dog"
print(convert_string(s))