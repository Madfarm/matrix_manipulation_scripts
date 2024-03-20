def permute_string(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = list(s)
    vowel_position = []
    vowels_list = []

    for i, char in enumerate(s):
        if s[i].lower() in vowels:
            vowels_list.append(s[i])
            vowel_position.append(i)


    vowels_list.sort()

    for position, vowel in zip(vowel_position, vowels_list):
         s[position] = vowel


    return ''.join(s)

# Test the function
s = "consOnAnt"
print(permute_string(s))  # Output: "cAnsOnont"