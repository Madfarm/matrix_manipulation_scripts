def validate_input(message):
    forbidden_words = ["cat", "pig", "mask", "hat", "trace", "open", "unfortunate"]
    punctuation = [".", ",", "!", "?"]

    if len(message) < 12:
        print("Message is too short.")

    if not any(p in message for p in punctuation):
        print("There's no punctuation in this message.")

    for word in forbidden_words:
        if word in message:
            print("Message contains forbidden words")
    
    print("end " + message)
    print("")

# Testing the function
validate_input("Hello world!")
validate_input("This is a test message")
validate_input("cat is a forbidden word")
validate_input("This message is too short and contains a forbidden word, cat")