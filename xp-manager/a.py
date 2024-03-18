import random

class Player:
    def __init__(self, level):
        self.level = 1
        self.experience = 0
        self.stats = {'strength': 5, 'health': 5, 'dexterity': 5, 'magic': 5}
        while self.level < level:
            self.level_up()

    def level_up(self):
        self.level += 1
        stat_to_increase = random.choice(list(self.stats.keys()))
        self.stats[stat_to_increase] += 1
        if self.level % 10 == 0:
            for _ in range(5):
                stat_to_increase = random.choice(list(self.stats.keys()))
                self.stats[stat_to_increase] += 1

    def add_experience(self, experience):
        self.experience += experience
        while self.experience >= self.level * 100:
            self.level_up()
            self.experience -= self.level * 100

player = Player(25)
print(player.level)
print(player.stats)
player.add_experience(500)
print(player.level)
print(player.stats)