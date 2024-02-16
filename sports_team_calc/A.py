import numpy as np
import itertools

# Helper functions
def satisfies_constraints(combination, roles, min_players_per_role, max_players_per_role):
    # Count the number of players in each role
    role_counts = [0] * len(roles)
    for player in combination:
        role_counts[roles.index(player['role'])] += 1
    
    # Check if the counts satisfy the constraints
    for i, (min_count, max_count) in enumerate(zip(min_players_per_role, max_players_per_role)):
        if role_counts[i] < min_count or role_counts[i] > max_count:
            return False
    return True

def calculate_score(combination, weights):
    # Calculate the weighted sum of the players' statistics
    score = 0
    for player in combination:
        for stat, weight in zip(player.values(), weights):
            score += weight * stat
    return score



# Define the team composition constraints
roles = ['GK', 'DF', 'MF', 'FW']
min_players_per_role = [1, 3, 4, 2]
max_players_per_role = [2, 5, 6, 3]

# Define the candidate players with their statistics and cost
players = [
    {'name': 'Player1', 'speed': 80, 'accuracy': 70, 'strength': 60, 'experience': 80, 'cost': 10000},
    {'name': 'Player2', 'speed': 90, 'accuracy': 60, 'strength': 70, 'experience': 70, 'cost': 12000},
    {'name': 'Player3', 'speed': 70, 'accuracy': 80, 'strength': 50, 'experience': 90, 'cost': 9000},
    # Add more players here...
]

# Define the weights for each statistic
weights = [0.3, 0.2, 0.15, 0.35]  # speed, accuracy, strength, experience

# Define the budget
budget = 50000

# Initialize the best team and its score
best_team = []
best_score = 0

# Iterate through all possible team combinations
for combination in itertools.combinations(players, len(roles)):
    # Check if the combination satisfies the team composition constraints
    if satisfies_constraints(combination, roles, min_players_per_role, max_players_per_role):
        # Calculate the total cost of the combination
        total_cost = sum(player['cost'] for player in combination)
        
        # Check if the combination is within budget
        if total_cost <= budget:
            # Calculate the overall performance score for the combination
            score = calculate_score(combination, weights)
            
            # Update the best team and its score if the current combination is better
            if score > best_score:
                best_team = combination
                best_score = score

# Print the best team and its score
print("Best Team:", [player['name'] for player in best_team])
print("Best Score:", best_score)

