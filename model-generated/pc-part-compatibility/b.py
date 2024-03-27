class ComputerPart:
    def __init__(self, voltage, size, memory):
        self.voltage = voltage
        self.size = size
        self.memory = memory

def check_compatibility(parts):
    # Get the first part as a reference
    ref_part = parts[0]

    # Check compatibility with the rest of the parts
    for part in parts[1:]:
        if part.voltage != ref_part.voltage:
            return False
        if part.size != ref_part.size:
            return False
        if part.memory != ref_part.memory:
            return False

    return True

# Create some computer parts
part1 = ComputerPart(12, '10cm', '8GB')
part2 = ComputerPart(12, '10cm', '8GB')
part3 = ComputerPart(12, '10cm', '8GB')
part4 = ComputerPart(12, '10cm', '8GB')

# Check compatibility
parts = [part1, part2, part3, part4]
print(check_compatibility(parts))  # Outputs: True

# Create some computer parts
part1 = ComputerPart(12, '10cm', '8GB')
part2 = ComputerPart(12, '10cm', '8GB')
part3 = ComputerPart(12, '10cm', '8GB')
part4 = ComputerPart(12, '10cm', '16GB')

# Check compatibility
parts = [part1, part2, part3, part4]
print(check_compatibility(parts))  # Outputs: False