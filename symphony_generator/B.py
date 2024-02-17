import random

# Define a dictionary to store the symphony data
symphonies = {}

# Function to generate a random symphony code
def generate_symphony_code():
    return '-'.join([''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4)) for _ in range(3)])

# Function to generate a random time signature
def generate_time_signature():
    num = random.randint(2, 7)
    denom = random.randint(2, 8)
    return f"{num}/{denom}"

# Function to generate a random key signature
def generate_key_signature():
    sharp_count = random.randint(0, 5)
    flat_count = random.randint(0, 5)
    key = ''
    for _ in range(sharp_count):
        key += '#'
    for _ in range(flat_count):
        key += 'b'
    return key

# Function to generate a random tempo
def generate_tempo():
    return random.randint(40, 120)

# Function to generate a random melody
def generate_melody(scale):
    melody = ''
    for _ in range(random.randint(10, 20)):
        note = random.choice(scale)
        melody += note
    return melody

# Function to generate a symphony
def generate_symphony():
    symphony_code = generate_symphony_code()
    movements = []
    for i in range(4):
        time_sig = generate_time_signature()
        key_sig = generate_key_signature()
        tempo = generate_tempo()
        scale = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        melody = generate_melody(scale)
        movement = {
            'time_sig': time_sig,
            'key_sig': key_sig,
            'tempo': tempo,
            'melody': melody
        }
        movements.append(movement)
    symphonies[symphony_code] = movements
    return symphony_code

# Generate 5 symphonies
for _ in range(5):
    generate_symphony()

# Print the first symphony
print(symphonies)