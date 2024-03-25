from cryptography.fernet import Fernet
import os

class RecipeManager:
    def __init__(self, key):
        self.key = key
        self.recipes = {}

    def add_recipe(self, name, recipe):
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(recipe.encode())
        self.recipes[name] = cipher_text

    def view_recipe(self, name):
        cipher_suite = Fernet(self.key)
        cipher_text = self.recipes[name]
        plain_text = cipher_suite.decrypt(cipher_text).decode()
        return plain_text

    def edit_recipe(self, name, new_recipe):
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(new_recipe.encode())
        self.recipes[name] = cipher_text

# Generate a key
key = Fernet.generate_key()

# Create a RecipeManager instance
manager = RecipeManager(key)

# Add a recipe
manager.add_recipe('Meatballs', 'Ingredients: ...\nInstructions: ...')

# View a recipe
print(manager.view_recipe('Meatballs'))

# Edit a recipe
manager.edit_recipe('Meatballs', 'New ingredients: ...\nNew instructions: ...')

# View the edited recipe
print(manager.view_recipe('Meatballs'))