class BoxScore:
    def __init__(self):
        self.teams = {}
        self.players = {}

    def parse_box_score(self, raw_data):
        # Assume raw_data is a dictionary with team name as key and a list of players' stats as value
        for team, players in raw_data.items():
            self.teams[team] = {
                'points': sum(player['points'] for player in players),
                'assists': sum(player['assists'] for player in players),
                'rebounds': sum(player['rebounds'] for player in players),
                'steals': sum(player['steals'] for player in players),
                'turnovers': sum(player['turnovers'] for player in players),
                'fouls': sum(player['fouls'] for player in players),
            }
            for player in players:
                self.players[player['name']] = player

    def get_most_points(self):
        return max(self.players, key=lambda player: self.players[player]['points'])

    def get_fewest_turnovers(self):
        return min(self.teams, key=lambda team: self.teams[team]['turnovers'])


# Example usage:
box_score = BoxScore()
raw_data = {
    'TeamA': [
        {'name': 'Player1', 'points': 20, 'assists': 5, 'rebounds': 6, 'steals': 3, 'turnovers': 2, 'fouls': 3},
        {'name': 'Player2', 'points': 15, 'assists': 4, 'rebounds': 5, 'steals': 2, 'turnovers': 3, 'fouls': 4},
    ],
    'TeamB': [
        {'name': 'Player3', 'points': 25, 'assists': 6, 'rebounds': 7, 'steals': 4, 'turnovers': 1, 'fouls': 2},
        {'name': 'Player4', 'points': 10, 'assists': 3, 'rebounds': 4, 'steals': 1, 'turnovers': 4, 'fouls': 5},
    ],
}
box_score.parse_box_score(raw_data)
print(box_score.get_most_points())  # Player3
print(box_score.get_fewest_turnovers())  # TeamB