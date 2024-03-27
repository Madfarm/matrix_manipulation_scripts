class BoxScore:
    def __init__(self):
        self.teams = {}

    def read_box_score(self, raw_string):
        # Assume raw_string is a string with team stats separated by commas
        # and individual player stats separated by spaces
        # Example format: "Team1 23 12 32, Team2 34 21 19"
        team_stats = raw_string.split(', ')
        for team_stat in team_stats:
            team, stats = team_stat.split(' ')
            self.teams[team] = list(map(int, stats))

    def get_statistical_breakdown(self, stat_type):
        if stat_type == 'points':
            return max(self.teams, key=lambda team: self.teams[team][0])
        elif stat_type == 'assists':
            return max(self.teams, key=lambda team: self.teams[team][1])
        elif stat_type == 'rebounds':
            return max(self.teams, key=lambda team: self.teams[team][2])
        else:
            return "Invalid stat type"

# Example usage
box_score = BoxScore()
box_score.read_box_score("Team1 89 32 45, Team2 91 28 42")
print(box_score.get_statistical_breakdown('points'))  # Output: Team2
print(box_score.get_statistical_breakdown('assists'))  # Output: Team1
print(box_score.get_statistical_breakdown('rebounds'))  # Output: Team1