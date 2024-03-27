import random

class Unicorn:
    def __init__(self, name, color, magic_skill_level):
        self.name = name
        self.color = color
        self.magic_skill_level = magic_skill_level

    def perform_magic(self):
        # Improve magic skill level by 10% after every successful magic trick
        self.magic_skill_level += 10
        if self.magic_skill_level > 100:
            self.magic_skill_level = 100

    def __str__(self):
        return f'{self.color} unicorn {self.name} with magic skill level {self.magic_skill_level}%'

def unicorn_race(unicorns):
    max_skill_level = max(unicorn.magic_skill_level for unicorn in unicorns)
    winner = random.choice([unicorn for unicorn in unicorns if unicorn.magic_skill_level == max_skill_level])
    return winner

# Create unicorns
unicorn1 = Unicorn('Sparkles', 'White', 20)
unicorn2 = Unicorn('Rainbow', 'Red', 40)
unicorn3 = Unicorn('Lightning', 'Blue', 60)
unicorns = [unicorn1, unicorn2, unicorn3]

# Perform magic tricks
for unicorn in unicorns:
    for _ in range(5):
        unicorn.perform_magic()

# Race
winner = unicorn_race(unicorns)
print(f'The winner of the race is {winner}')