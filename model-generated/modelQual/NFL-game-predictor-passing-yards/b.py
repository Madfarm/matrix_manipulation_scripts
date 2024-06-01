import random

def predict_game_outcome(quarterback1, quarterback2):
    # Assume the quarterback with the higher passing yards has a 60% chance of winning
    if quarterback1['passing_yards'] > quarterback2['passing_yards']:
        return quarterback1['name']
    elif quarterback2['passing_yards'] > quarterback1['passing_yards']:
        return quarterback2['name']
    else:
        # If the passing yards are equal, the outcome is random
        return random.choice([quarterback1['name'], quarterback2['name']])

# Define the quarterbacks
brock_purdy = {'name': 'Brock Purdy', 'passing_yards': 4280}
patrick_mahomes = {'name': 'Patrick Mahomes', 'passing_yards': 4183}

# Predict the outcome of the game
winner = predict_game_outcome(brock_purdy, patrick_mahomes)

print(f'The winner of the game is: {winner}')