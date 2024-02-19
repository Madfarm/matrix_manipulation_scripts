
class Dinosaur:
    def __init__(self, reproduction_rate, lifespan, initial_population):
        self.reproduction_rate = reproduction_rate
        self.lifespan = lifespan
        self.population = initial_population
        self.growth_rate = 0
    
    def grow(self, temperature, food_availability):
        # Simulate growth based on temperature and food availability
        self.growth_rate = self.reproduction_rate * (temperature / 100) * (food_availability / 100)
        self.population += self.growth_rate
    
    def die_off(self, temperature, food_availability):
        # Simulate die-off based on temperature and food availability
        die_off_rate = (1 - (temperature / 100)) * (1 - (food_availability / 100))
        self.population -= self.population * die_off_rate
    
    def update(self, temperature, food_availability):
        self.grow(temperature, food_availability)
        self.die_off(temperature, food_availability)
        self.population = max(0, self.population)  # prevent negative population
    
    def predict_population(self, years, temperature_changes, food_availability_changes):
        for year in range(years):
            for temp_change in temperature_changes:
                self.update(temp_change, food_availability_changes[year])
            self.update(temperature_changes[-1], food_availability_changes[year])
        return self.population

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        reproduction_rate = float(file.readline().strip())
        lifespan = int(file.readline().strip())
        initial_population = int(file.readline().strip())
        years = int(file.readline().strip())
        temperature_changes = [float(line.strip()) for line in file.readlines()]
        food_availability_changes = [float(line.strip()) for line in file.readlines()]
        return reproduction_rate, lifespan, initial_population, years, temperature_changes, food_availability_changes

def main():
    print("Do you want to input values manually or read from a file? (file/manual)")
    input_method = input()
    if input_method == 'file':
        filename = input("Enter file name: ")
        reproduction_rate, lifespan, initial_population, years, temperature_changes, food_availability_changes = read_input_from_file(filename)
    else:
        reproduction_rate = float(input("Enter reproduction rate: "))
        lifespan = int(input("Enter lifespan: "))
        initial_population = int(input("Enter initial population: "))
        years = int(input("Enter number of years to predict: "))
        temperature_changes = [float(input(f"Enter temperature change for year {i+1}: ")) for i in range(years)]
        food_availability_changes = [float(input(f"Enter food availability change for year {i+1}: ")) for i in range(years)]

    dino = Dinosaur(reproduction_rate, lifespan, initial_population)
    predicted_population = dino.predict_population(years, temperature_changes, food_availability_changes)
    print(f"Predicted population after {years} years: {predicted_population}")

if __name__ == "__main__":
    main()