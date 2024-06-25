class Shoe:
    def __init__(self, name, color, breathability, weight):
        self.name = name
        self.color = color
        self.breathability = breathability
        self.weight = weight

def shoe_lookup(criteria):
    assert criteria in ["color", "breathability", "weight"], "Invalid criteria"

    shoes = [
        Shoe("Messi Samba", "Red", 0.5, 300),
        Shoe("Nike Air Force 1 Low NY vs. NY (2024)", "Blue", 0.7, 350),
        Shoe("Puma Mostro (2024)", "Green", 0.6, 320),
        Shoe("Li-Ning Way of Wade 11 305", "Yellow", 0.8, 380)
    ]

    if criteria == "color":
        return sorted(shoes, key=lambda shoe: shoe.color)
    elif criteria == "breathability":
        return sorted(shoes, key=lambda shoe: shoe.breathability, reverse=True)
    elif criteria == "weight":
        return sorted(shoes, key=lambda shoe: shoe.weight)

# Test the function
print(shoe_lookup("color"))
print(shoe_lookup("breathability"))
print(shoe_lookup("weight"))