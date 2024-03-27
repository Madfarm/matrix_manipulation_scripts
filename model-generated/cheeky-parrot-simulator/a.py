def parrot_conversation(query):
    vocabulary = {
        "animals": ["lion", "tiger", "elephant", "monkey"],
        "history": ["rome", "egypt", "china", "greece"],
        "geography": ["africa", "asia", "europe", "australia"]
    }

    # Parrot's cheeky responses
    responses = {
        "animals": "Squawk! You want to know about animals? Okay... but can you give me a treat first?",
        "history": "Arf! History, you say? Well, I know a thing or two about that... if you can find the right treats, that is.",
        "geography": "Polly want a cracker! Where are we talking about, exactly? Can you give me a hint?"
    }

    # Parsing the query
    query_words = query.lower().split()
    topic = None
    print(vocabulary.values())
    for word in query_words:
        if word in vocabulary.values():
            topic = word
            break

    if topic:
        # Check if the query contains any words from the vocabulary
        relevant_words = [word for word in query_words if word in vocabulary[topic]]
        if relevant_words:
            return f"{responses[topic]} I know a lot about {', '.join(relevant_words)}!"
        else:
            return f"{responses[topic]} But I'm not sure about that specific topic."
    else:
        return "Squawk! What are you trying to ask me? Can't you see I'm busy preening my feathers?"

# Testing the function
print(parrot_conversation("Can you tell me about lions?"))
print(parrot_conversation("What's the capital of Egypt?"))
print(parrot_conversation("Where is Australia located?"))
print(parrot_conversation("I want to know about dogs."))

