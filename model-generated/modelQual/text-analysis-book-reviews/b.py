import re
from collections import Counter

def word_analysis(text1, text2):
    # Convert both texts to lowercase
    text1 = text1.lower()
    text2 = text2.lower()

    # Remove punctuation and pronouns
    text1 = re.sub(r'[^\w\s]', '', text1)
    text2 = re.sub(r'[^\w\s]', '', text2)
    pronouns = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them']
    for pronoun in pronouns:
        text1 = text1.replace(pronoun, '')
        text2 = text2.replace(pronoun, '')

    # Split the texts into words
    words1 = text1.split()
    words2 = text2.split()

    # Remove common words
    common_words = ['the', 'a', 'an', 'in', 'on', 'at', 'by', 'with', 'from', 'to', 'of', 'and', 'or', 'but', 'not', 'is', 'are', 'am', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should', 'can', 'could', 'may', 'might', 'must', 'need', 'ought', 'shall', 'should', 'will', 'would']
    for word in common_words:
        words1 = [w for w in words1 if w != word]
        words2 = [w for w in words2 if w != word]

    # Count the occurrences of each word
    counter1 = Counter(words1)
    counter2 = Counter(words2)

    # Combine the counters into a dictionary
    result = {}
    for word in set(list(counter1.keys()) + list(counter2.keys())):
        result[word] = (counter1.get(word, 0), counter2.get(word, 0))

    return result

# Test the function
text1 = "a romance novel that has received positive reviews for its witty and sensitive portrayal of relationships and intimacy. The book follows the story of two characters, Daphne and Miles, as they navigate their feelings for each other and confront their past traumas. "
text2 = "a thriller novel by Ashley Elston that has received positive reviews for its suspenseful plot and engaging characters. The book follows the story of a woman named Evie who is on the run from her past and must use her wits to stay one step ahead of her pursuers. The novel has been praised for its clever twists and turns, as well as its romantic elements"
print(word_analysis(text1, text2))