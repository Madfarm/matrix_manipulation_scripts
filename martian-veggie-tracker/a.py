class Vegetable:
    def __init__(self, name, SolsToMature, waterPerSol):
        self.name = name
        self.SolsToMature = SolsToMature
        self.waterPerSol = waterPerSol
        self.growthDays = 0
        self.isMature = False

    def check_status(self):
        if self.isMature:
            print(f'{self.name} are ready to harvest!')
        elif self.growthDays == self.SolsToMature:
            self.isMature = True
            print(f'{self.name} are mature and ready to harvest!')
        else:
            daysLeft = self.SolsToMature - self.growthDays
            print(f'{self.name} need {daysLeft} more days to mature.')

    def water(self, waterSupply):
        if waterSupply >= self.waterPerSol:
            self.growthDays += 1
            print(f'{self.name} have been watered.')
        else:
            print('Not enough water to water the plant.')

    def harvest(self):
        if self.isMature:
            print(f'{self.name} have been harvested.')
            self.isMature = False
            self.growthDays = 0
        else:
            print(f'{self.name} are not mature yet.')


# Creating instances of Vegetable class
potato = Vegetable('Potato', 5, 3)
pea = Vegetable('Pea', 3, 2)
carrot = Vegetable('Carrot', 4, 2)

# Watering and checking status
potato.water(3)
potato.check_status()  # Potato need 2 more days to mature.
pea.water(2)
pea.check_status()  # Pea need 1 more day to mature.
carrot.water(2)
carrot.check_status()  # Carrot need 2 more days to mature.

# Watering again and checking status
potato.water(3)
potato.check_status()  # Potato are mature and ready to harvest!
pea.water(2)
pea.check_status()  # Pea are mature and ready to harvest!
carrot.water(2)
carrot.check_status()  # Carrot are mature and ready to harvest!

# Harvesting
potato.harvest()  # Potato have been harvested.
pea.harvest()  # Pea have been harvested.
carrot.harvest()  # Carrot have been harvested.