atomic_masses = {
    "H": 1.008,
    "He": 4.0026,
    "Li": 6.94,
    "Be": 9.0122,
    "B": 10.81,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Ne": 20.180,
    "Na": 22.98976928,
}

def calculate_molar_mass(formula):
    # Split the formula into elements and their counts
    elements = []
    current_element = ""
    current_count = ""
    for char in formula:
        if char.isupper():
            if current_element:
                elements.append((current_element, int(current_count) if current_count else 1))
            current_element = char
            current_count = ""
        elif char.islower():
            current_element += char
        elif char.isdigit():
            current_count += char
    if current_element:
        elements.append((current_element, int(current_count) if current_count else 1))

    # Calculate the molar mass
    molar_mass = 0
    for element, count in elements:
        molar_mass += atomic_masses[element] * count

    return molar_mass

# Test the script using sodium glutamate: C5H8NNaO4
print(calculate_molar_mass("C5H8NNaO4"))