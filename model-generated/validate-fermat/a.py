def validate_theorem(species):
    for a in species:
        for b in species:
            for c in species:
                for n in range(3, 100):  # assuming the ages won't be too large
                    if (a ** n + b ** n == c ** n) and (a != b != c):
                        return False
    return True


species = [50, 21, 150]  # ages of Elephant, Hawk and Tortoise
print(validate_theorem(species))