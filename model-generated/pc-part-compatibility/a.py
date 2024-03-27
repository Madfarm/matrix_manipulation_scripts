class ComputerPart:
    def __init__(self, voltage, size, memory):
        self.voltage = voltage
        self.size = size
        self.memory = memory

def are_compatible(part1, part2):
    if part1.voltage == part2.voltage and part1.size == part2.size and part1.memory == part2.memory:
        return True
    else:
        return False

# create two parts
part1 = ComputerPart(12, 'small', '1GB')
part2 = ComputerPart(12, 'small', '1GB')
part3 = ComputerPart(12, 'large', '2GB')

# check compatibility
print(are_compatible(part1, part2))  # True
print(are_compatible(part1, part3))  # False