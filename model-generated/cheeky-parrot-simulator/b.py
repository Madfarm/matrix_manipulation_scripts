def parrot_conversation(query):
    vocabulary = {
        "animals": {
            "lion": "The king of the jungle, roars loudly.",
            "elephant": "Large and grey, has a great memory.",
            "cheetah": "Fastest land animal, spotted legs."
        },
        "history": {
            "rome": "Ancient city with lots of ruins.",
            "egypt": "Land of the pharaohs, famous for pyramids.",
            "greece": "Home of democracy, famous philosophers."
        },
        "geography": {
            "australia": "Large country with beautiful beaches.",
            "canada": "Nice maple leaves, famous for hockey.",
            "japan": "Land of the rising sun, known for anime."
        }
    }

    query_words = query.lower().split()
    topic = query_words[0]
    entity = " ".join(query_words[1:])

    if topic in vocabulary and entity in vocabulary[topic]:
        return vocabulary[topic][entity]
    else:
        return "I don't know about that."

# Test the function
print(parrot_conversation("animals lion"))  # Output: The king of the jungle, roars loudly.
print(parrot_conversation("history rome"))  # Output: Ancient city with lots of ruins.
print(parrot_conversation("geography australia"))  # Output: Large country with beautiful beaches.
print(parrot_conversation("animals dog"))  # Output: I don't know about that.