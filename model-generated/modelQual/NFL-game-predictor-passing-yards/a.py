import random

def predict_game_outcome(player1, player2):
    # Generate a random number between 0 and 1
    random_number = random.random()

    # If the random number is less than 0.5, player1 wins
    if random_number < 0.5:
        return f"{player1} wins!"
    # Otherwise, player2 wins
    else:
        return f"{player2} wins!"

# Test the function
print(predict_game_outcome("Brock Purdy", "Patrick Mahomes"))