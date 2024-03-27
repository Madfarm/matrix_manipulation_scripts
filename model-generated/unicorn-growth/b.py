class Unicorn:
    def __init__(self, name, color, magic_skill_level):
        self.name = name
        self.color = color
        self.magic_skill_level = magic_skill_level

    def perform_magic(self):
        self.magic_skill_level += 10
        if self.magic_skill_level > 100:
            self.magic_skill_level = 100
        print(f"{self.name} has performed a magic trick and improved their magic skill level to {self.magic_skill_level}%.")

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Magic Skill Level: {self.magic_skill_level}%"

def unicorn_race(unicorns):
    max_skill_level = max(unicorn.magic_skill_level for unicorn in unicorns)
    winners = [unicorn for unicorn in unicorns if unicorn.magic_skill_level == max_skill_level]

    if len(winners) == 1:
        print(f"The winner of the race is {winners[0].name} with a magic skill level of {winners[0].magic_skill_level}%!")
    else:
        print(f"It's a tie between {', '.join(winner.name for winner in winners)} with a magic skill level of {winners[0].magic_skill_level}%!")

# Create unicorns
unicorn1 = Unicorn("Sparkles", "White", 20)
unicorn2 = Unicorn("Rainbow", "Purple", 30)
unicorn3 = Unicorn("Glitter", "Gold", 10)

# Perform magic tricks
unicorn1.perform_magic()
unicorn2.perform_magic()
unicorn3.perform_magic()

# Race
unicorns = [unicorn1, unicorn2, unicorn3]
unicorn_race(unicorns)