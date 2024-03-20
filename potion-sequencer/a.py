class PotionMaker:
    def __init__(self):
        # Dictionary to store potions and their ingredient sequences
        self.potions = {}

    def load_potion(self, potion_name, ingredient_sequence):
        # Add a potion to the dictionary with its ingredient sequence
        self.potions[potion_name] = ingredient_sequence

    def create_potion(self, potion_name, ingredients):
        # Check if the potion exists in the dictionary
        if potion_name in self.potions:
            # Get the ingredient sequence for the potion
            ingredient_sequence = self.potions[potion_name]
            # Check if the ingredients match the sequence
            if ingredients == ingredient_sequence:
                # Print each step of the creation
                for ingredient in ingredients:
                    print(f"Adding {ingredient} to the potion")
                print(f"Potion {potion_name} created successfully!")
            else:
                print("Error: Invalid ingredient sequence")
        else:
            print("Error: Potion not found")

# Create a PotionMaker instance
potion_maker = PotionMaker()

# Load some potions
potion_maker.load_potion("Potion of Healing", ["Herb of Life", "Blood of Unicorn", "Water of Life"])
potion_maker.load_potion("Potion of Strength", ["Root of Strength", "Elixir of Power", "Gem of Fortitude"])

# Try to create a potion
potion_maker.create_potion("Potion of Healing", ["Herb of Life", "Blood of Unicorn", "Water of Life"])

# Try to create a potion with an invalid sequence
potion_maker.create_potion("Potion of Healing", ["Blood of Unicorn", "Herb of Life", "Water of Life"])

# Try to create a potion that doesn't exist
potion_maker.create_potion("Potion of Weakness", ["Root of Weakness", "Elixir of Frailty", "Gem of Cowardice"])