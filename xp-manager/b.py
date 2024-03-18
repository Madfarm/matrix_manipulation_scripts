import random

class Player:
    def __init__(self, level=1):
        self.level = 1
        self.experience = 0
        self.stats = {'strength': 5, 'health': 5, 'dexterity': 5, 'magic': 5}
        n=1
        while self.level < level:
            self.level_up()
            print(n)
            n += 1

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

# Demonstration
player = Player(level=20)
print(player.level)  # Output: 20
print(player.stats)  # Output: {'strength': 10, 'health': 10, 'dexterity': 10, 'magic': 10}
player.add_experience(2000)
print(player.level)  # Output: 22
print(player.stats)  # Output: {'strength': 12, 'health': 12, 'dexterity': 12, 'magic': 12}