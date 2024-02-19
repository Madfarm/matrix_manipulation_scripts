import random

class Dinosaur:
    def __init__(self, reproduction_rate, lifespan, initial_population):
        self.reproduction_rate = reproduction_rate
        self.lifespan = lifespan
        self.population = initial_population
        self.death_rate = 0

    def update_population(self, temperature_change, food_scarcity):
        # adjust reproduction rate based on temperature change
        self.reproduction_rate *= 1 + (temperature_change / 10)
        
        # adjust death rate based on food scarcity
        self.death_rate += (food_scarcity / 10)
        
        # simulate population change
        births = self.reproduction_rate * self.population
        deaths = self.death_rate * self.population
        self.population += births - deaths
        
        # apply natural mortality ( assuming a constant rate)
        self.population -= (self.population / self.lifespan)

    def predict_population(self, years, temperature_changes, food_scarcity_list):
        for year in range(years):
            for change in temperature_changes:
                self.update_population(change, food_scarcity_list[year])
            self.population = int(self.population)  # round to nearest integer
        return self.population

# example usage:
dinosaur = Dinosaur(2, 50, 1000)  # reproduction rate, lifespan, initial population

# define environmental parameters
years = 50
temperature_changes = [0.5, -1.2, 0.8, -0.4]  # degrees Celsius
food_scarcity_list = [0.2, 0.1, 0.3, 0.4, 0.5]  # scales from 0 to 1

# predict population decline
final_population = dinosaur.predict_population(years, temperature_changes, food_scarcity_list)
print("Final population:", final_population)