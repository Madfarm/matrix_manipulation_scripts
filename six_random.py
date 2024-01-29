import random

random_numbers = []
while len(random_numbers) < 6:
    new_number = random.randint(1, 100)
    if new_number not in random_numbers:
        random_numbers.append(new_number)

print(random_numbers)