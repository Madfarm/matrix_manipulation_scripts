def calculate_damage(characters):
    damage = {}
    for character in characters:
        burst_damage = characters[character]['Elemental Burst'] * 1000
        skill_damage = characters[character]['Elemental Skill'] * 500
        total_damage = burst_damage + skill_damage
        damage[character] = total_damage
    return damage

characters = {
    'Xingqiu': {'Elemental Burst': 1.5, 'Elemental Skill': 0.5},
    # Add more characters as needed
}

damage = calculate_damage(characters)
print(damage)