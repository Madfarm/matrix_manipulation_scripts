class Vegetable:
    def __init__(self, name, SolsToMature, waterPerSol):
        self.name = name
        self.SolsToMature = SolsToMature
        self.waterPerSol = waterPerSol
        self.growthDays = 0

    def check_status(self):
        if self.growthDays < self.SolsToMature:
            print(f"{self.name} is not yet mature. {self.SolsToMature - self.growthDays} days to go.")
        else:
            print(f"{self.name} is mature and ready to harvest.")

    def water(self):
        if self.growthDays < self.SolsToMature:
            self.growthDays += 1
            print(f"{self.name} has been watered. {self.SolsToMature - self.growthDays} days to go.")
        else:
            print(f"{self.name} is already mature. No need to water.")

    def harvest(self):
        if self.growthDays >= self.SolsToMature:
            print(f"{self.name} has been harvested.")
            self.growthDays = 0  # Resetting growth days for the next harvest
        else:
            print(f"{self.name} is not yet mature. Please wait.")


# Creating objects of Vegetable class
potato = Vegetable("Potato", 5, 1)
pea = Vegetable("Pea", 3, 2)
carrot = Vegetable("Carrot", 4, 1.5)

# Checking initial status of each vegetable
potato.check_status()
pea.check_status()
carrot.check_status()

# Watering each vegetable for 4 Sols
for _ in range(4):
    potato.water()
    pea.water()
    carrot.water()

# Checking the status of each vegetable after watering
potato.check_status()
pea.check_status()
carrot.check_status()

# Harvesting each vegetable
potato.harvest()
pea.harvest()
carrot.harvest()

