from itertools import combinations
import numpy as np

def weighted_sum(stats, weights):
    return np.dot(stats, weights)

def team_performance(team, stats, weights):
    return weighted_sum(np.array(team).T @ stats, weights)

def team_cost(team):
    return np.sum(team[:, 1])

def compose_team(candidates, roles, min_players, max_players, budget, weights):
    # Filter candidates by role and cost
    filtered_candidates = []
    for role in roles:
        candidates_in_role = [c for c in candidates if c[2] == role]
        candidates_in_role.sort(key=lambda x: x[1])  # Sort by cost
        filtered_candidates.extend(candidates_in_role[:max_players[role]])
    
    # Compute all possible team combinations
    teams = list(combinations(filtered_candidates, len(roles)))
    
    # Filter teams by budget and composition constraints
    valid_teams = []
    for team in teams:
        if team_cost(team) <= budget and all(min_players[role] <= team.count(role) <= max_players[role] for role in roles):
            valid_teams.append(team)
    
    # Compute performance scores for valid teams
    performance_scores = [team_performance(team, stats, weights) for team in valid_teams]
    
    # Return the team with the highest performance score
    return valid_teams[np.argmax(performance_scores)]

# Example usage
stats = np.array([
    [10, 5, 3, 8, 2],  # Speed, Accuracy, Strength, Experience, Other
    [8, 6, 4, 5, 1],
    [6, 8, 5, 7, 3],
    [4, 9, 2, 6, 4],
    [7, 4, 6, 3, 5],
    [5, 7, 8, 4, 2],
    [9, 3, 1, 2, 6],
    [2, 1, 9, 1, 8],
    [3, 2, 7, 9, 1],
])
weights = np.array([0.4, 0.3, 0.1, 0.1, 0.1])  # Weights for each statistic

roles = ['Defender', 'Midfielder', 'Forward']
min_players = {'Defender': 3, 'Midfielder': 4, 'Forward': 3}
max_players = {'Defender': 5, 'Midfielder': 6, 'Forward': 5}
budget = 100  # Team budget in thousands

candidates = [
    [10, 5, 'Defender', 10],
    [8, 6, 'Defender', 8],
    [6, 8, 'Midfielder', 7],
    [4, 9, 'Midfielder', 6],
    [7, 4, 'Forward', 5],
    [5, 7, 'Forward', 4],
    [9, 3, 'Defender', 3],
    [2, 1, 'Midfielder', 2],
    [3, 2, 'Forward', 1],
]

team = compose_team(candidates, roles, min_players, max_players, budget, weights)
print(team)