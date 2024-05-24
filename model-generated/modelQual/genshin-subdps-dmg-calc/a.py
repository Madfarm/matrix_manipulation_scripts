def calculate_damage(characters):
    damage = {}
    for character in characters:
        name = character['name']
        elemental_burst = character['elemental_burst']
        elemental_skill = character['elemental_skill']
        damage[name] = (elemental_burst * 1000) + (elemental_skill * 500)
    return damage

# Test the function
characters = [
    {'name': 'Xingqiu', 'elemental_burst': 1.5, 'elemental_skill': 0.5},
    {'name': 'Childe', 'elemental_burst': 2.0, 'elemental_skill': 0.3},
    {'name': 'Xiao', 'elemental_burst': 1.8, 'elemental_skill': 0.4}
]
print(calculate_damage(characters))