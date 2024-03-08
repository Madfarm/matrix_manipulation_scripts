def validate_input(message):
    if len(message) < 12:
        print("Message is too short.")
    if not any(char in message for char in [".", ",", "!", "?", "-"]):
        print("There's no punctuation in this message.")
    forbidden_words = ["cat", "pig", "mask", "hat", "trace", "open", "unfortunate"]
    for word in forbidden_words:
        if word in message:
            print("Message contains forbidden words")
    print("end " + message)
    print("")


# Test the function
validate_input("Hello world!")
validate_input("Hello world")
validate_input("Hello world, how are you?")
validate_input("cat is a forbidden word")
validate_input("This message is too short and contains forbidden words, such as pig and mask.")