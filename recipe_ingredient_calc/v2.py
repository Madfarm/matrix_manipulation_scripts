def adjust_recipe(ingredients, original_servings, new_servings):
  """
  Adjusts ingredient quantities in a recipe based on a new desired serving size.

  Args:
    ingredients: A list of dictionaries, where each dictionary contains the
      ingredient name and quantity.
    original_servings: The original number of servings in the recipe.
    new_servings: The desired new number of servings.

  Returns:
    A list of dictionaries with adjusted ingredient quantities.
  """

  # Calculate the scaling factor for ingredient quantities.
  scaling_factor = new_servings / original_servings

  # Adjust ingredient quantities and return the updated recipe.
  return [
      {"ingredient": ingredient["ingredient"], "quantity": ingredient["quantity"] * scaling_factor}
      for ingredient in ingredients
  ]

# Example usage
recipe = [
    {"ingredient": "Flour", "quantity": 2.5},
    {"ingredient": "Sugar", "quantity": 1.0},
    {"ingredient": "Eggs", "quantity": 2},
    {"ingredient": "Milk", "quantity": 1.0},
]

original_servings = 4
new_servings = 6

adjusted_recipe = adjust_recipe(recipe, original_servings, new_servings)

print("Original recipe (", original_servings, " servings):")
for ingredient in recipe:
  print(f"\t{ingredient['ingredient']}: {ingredient['quantity']}")

print("\nAdjusted recipe (", new_servings, " servings):")
for ingredient in adjusted_recipe:
  print(f"\t{ingredient['ingredient']}: {ingredient['quantity']}")