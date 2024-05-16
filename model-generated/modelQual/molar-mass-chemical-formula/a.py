def calculate_molar_mass(formula, atomic_masses):
    # Initialize the molar mass to 0
    molar_mass = 0

    # Split the formula into elements and their counts
    elements = []
    current_element = ""
    for char in formula:
        if char.isupper():
            if current_element:
                elements.append(current_element)
            current_element = char
        else:
            current_element += char
    elements.append(current_element)

    # Calculate the molar mass
    for element in elements:
        symbol = element[0].upper()
        count = int(element[1:]) if len(element) > 1 else 1
        molar_mass += atomic_masses[symbol] * count

    return molar_mass

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

formula = "C5H8NNaO4"
print(calculate_molar_mass(formula, atomic_masses))