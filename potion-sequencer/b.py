# Initialize a dictionary to store potions and their ingredient sequences
potion_dict = {
    'Potion A': ['Ingredient 1', 'Ingredient 2', 'Ingredient 3'],
    'Potion B': ['Ingredient 2', 'Ingredient 1', 'Ingredient 3'],
    'Potion C': ['Ingredient 3', 'Ingredient 2', 'Ingredient 1']
}

# Function to check if a potion is successfully created
def check_potion(potion, ingredients):
    # Check if the potion exists in the dictionary
    if potion in potion_dict:
        # Check if the ingredients match the potion's recipe
        if potion_dict[potion] == ingredients:
            # Print the creation steps
            for i, ingredient in enumerate(ingredients, 1):
                print(f'Step {i}: Add {ingredient}')
            print(f'Congratulations! You have successfully created {potion}.')
        else:
            print('Error: The ingredients do not match the recipe for this potion.')
    else:
        print('Error: This potion does not exist in the dictionary.')

# Example usage
check_potion('Potion A', ['Ingredient 1', 'Ingredient 2', 'Ingredient 3'])
check_potion('Potion B', ['Ingredient 2', 'Ingredient 1', 'Ingredient 3'])
check_potion('Potion C', ['Ingredient 3', 'Ingredient 2', 'Ingredient 1'])
check_potion('Potion D', ['Ingredient 1', 'Ingredient 2', 'Ingredient 3'])
check_potion('Potion A', ['Ingredient 1', 'Ingredient 3', 'Ingredient 2'])