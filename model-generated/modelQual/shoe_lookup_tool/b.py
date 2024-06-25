class Shoe:
    def __init__(self, name, color, breathability, weight):
        self.name = name
        self.color = color
        self.breathability = breathability
        self.weight = weight
    def __repr__(self):
        return f"Name: {self.name}, Color: {self.color}, Breathability: {self.breathability}, Weight: {self.weight}"

def shoe_lookup(criteria):
    assert criteria in ["color", "breathability", "weight"], "Invalid criteria"
    
    shoes = [
        Shoe("Messi Sambas", "Red", 8, 250),
        Shoe("Nike Air Force 1 Low NY vs. NY (2024)", "Black", 9, 280),
        Shoe("Puma Mostro (2024)", "Blue", 7, 220),
        Shoe("Li-Ning Way of Wade 11 305", "Green", 8, 260)
    ]
    
    if criteria == "color":
        return sorted(shoes, key=lambda x: x.color)
    elif criteria == "breathability":
        return sorted(shoes, key=lambda x: x.breathability, reverse=True)
    elif criteria == "weight":
        return sorted(shoes, key=lambda x: x.weight)

# Test the function
print(shoe_lookup("color"))
print(shoe_lookup("breathability"))
print(shoe_lookup("weight"))