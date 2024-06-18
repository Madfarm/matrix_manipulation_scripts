import re

def count_words(text1, text2):
    # Convert both texts to lowercase
    text1 = text1.lower()
    text2 = text2.lower()

    # Remove words like "the", "a", and "an" as well as pronouns
    text1 = re.sub(r'\b(the|a|an|he|she|it|they|them|their|his|her)\b', '', text1)
    text2 = re.sub(r'\b(the|a|an|he|she|it|they|them|their|his|her)\b', '', text2)

    # Split the texts into words
    words1 = text1.split()
    words2 = text2.split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Count the occurrences of each word in both texts
    for word in words1:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    for word in words2:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Test the function with the given strings
text1 = "Great Expectations charts the progress of Pip from childhood through often painful experiences to adulthood, as he moves from the Kent marshes to busy, commercial London, encountering a variety of extraordinary characters"
text2 = "Brave New World, a dystopian novel, is often among the top 50 on Best Novel lists. It has stood the test of time. In addition, it's a fascinating take on what might happen to our society"

print(count_words(text1, text2))