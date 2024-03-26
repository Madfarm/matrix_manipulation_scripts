class Player:
    def __init__(self, name):
        self.name = name
        self.goals = 0
        self.assists = 0
        self.passes = 0
        self.interceptions = 0
        self.tackles = 0
        self.dribbles = 0
        self.shots_on_goal = 0

    def update_stats(self, goals, assists, passes, interceptions, tackles, dribbles, shots_on_goal):
        self.goals += goals
        self.assists += assists
        self.passes += passes
        self.interceptions += interceptions
        self.tackles += tackles
        self.dribbles += dribbles
        self.shots_on_goal += shots_on_goal

    def effectiveness_index(self):
        return (self.goals * 5) + (self.assists * 4) + (self.passes * 0.02) + (self.interceptions * 3) + (self.tackles * 3) + (self.dribbles * 0.5) + (self.shots_on_goal)

# create a player
player1 = Player("John Doe")

# update player's stats
player1.update_stats(5, 3, 100, 2, 5, 10, 20)

# print player's effectiveness index
print(player1.effectiveness_index())