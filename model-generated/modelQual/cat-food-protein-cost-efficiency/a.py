class CatFood:
    def __init__(self, brand, price, protein):
        self.brand = brand
        self.price = price
        self.protein = protein

def calculate_efficiency(cat_foods):
    # Calculate the efficiency of each cat food
    efficiencies = []
    for cat_food in cat_foods:
        efficiency = cat_food.protein / cat_food.price
        efficiencies.append((efficiency, cat_food.brand))
    return efficiencies

def rank_efficiencies(efficiencies):
    # Rank the efficiencies in descending order
    efficiencies.sort(reverse=True)
    return efficiencies

def print_rankings(efficiencies):
    # Print the rankings
    for i, (efficiency, brand) in enumerate(efficiencies, start=1):
        print(f"{i}. {brand} - Efficiency: {efficiency:.2f}")

# Create a list of cat foods
cat_foods = [
    CatFood("Purina", 2.99, 30),
    CatFood("Fancy Feast", 3.99, 40),
    CatFood("Whiskas", 1.99, 20),
    CatFood("Meow Mix", 2.49, 35)
]

# Calculate and rank the efficiencies
efficiencies = calculate_efficiency(cat_foods)
ranked_efficiencies = rank_efficiencies(efficiencies)

# Print the rankings
print_rankings(ranked_efficiencies)

