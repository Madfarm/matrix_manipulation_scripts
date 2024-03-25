from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Initialize an empty dictionary to store recipes
recipes = {}

def add_recipe(name, recipe):
    # Encrypt the recipe before storing it
    encrypted_recipe = cipher_suite.encrypt(recipe.encode())
    recipes[name] = encrypted_recipe

def view_recipe(name):
    # Decrypt the recipe before displaying it
    encrypted_recipe = recipes[name]
    decrypted_recipe = cipher_suite.decrypt(encrypted_recipe).decode()
    print(decrypted_recipe)

def edit_recipe(name, new_recipe):
    # Decrypt the existing recipe, then encrypt the new recipe
    encrypted_recipe = recipes[name]
    decrypted_recipe = cipher_suite.decrypt(encrypted_recipe).decode()
    
    if decrypted_recipe == new_recipe:
        print("New recipe is the same as the original - no edits were made")
        return
   
    encrypted_new_recipe = cipher_suite.encrypt(new_recipe.encode())
    recipes[name] = encrypted_new_recipe

# Add a recipe
add_recipe("Grandma's Meatloaf", "1 lb ground beef, 1 onion, 2 cloves garlic, 1 cup ketchup, 1 tbsp brown sugar, 1 tsp dried thyme, 1 tsp salt, 1/2 tsp black pepper, 1/4 cup Worcestershire sauce")

# View the recipe
view_recipe("Grandma's Meatloaf")

# Edit the recipe
edit_recipe("Grandma's Meatloaf", "1 lb ground beef, 1 onion, 2 cloves garlic, 1 cup ketchup, 1 tbsp brown sugar, 1 tsp dried thyme, 1 tsp salt, 1/2 tsp black pepper, 1/4 cup Worcestershire sauce, 1 egg")

# View the edited recipe
view_recipe("Grandma's Meatloaf")