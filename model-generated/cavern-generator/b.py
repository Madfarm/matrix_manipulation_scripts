import random

def create_cavern(width, height, depth):
    cavern = [[[' ' for _ in range(width)] for _ in range(height)] for _ in range(depth)]

    # Add some walls
    for z in range(depth):
        for y in range(height):
            for x in range(width):
                if random.random() < 0.2:
                    cavern[z][y][x] = '#'

    # Add some underwater sections
    for z in range(depth):
        for y in range(height):
            for x in range(width):
                if random.random() < 0.1:
                    cavern[z][y][x] = '~'

    # Add some paths
    for z in range(depth):
        for y in range(height):
            for x in range(width):
                if random.random() < 0.05:
                    cavern[z][y][x] = '.'

    return cavern

def print_cavern(cavern):
    for z in range(len(cavern)):
        print(f"Depth {z}:")
        for y in range(len(cavern[z])):
            print(''.join(cavern[z][y]))
        print()

def explore_cavern(cavern):
    x, y, z = random.randint(0, len(cavern[0][0])-1), random.randint(0, len(cavern[0])-1), random.randint(0, len(cavern)-1)
    while True:
        print(f"You are at position ({x}, {y}, {z})")
        print_cavern(cavern)
        direction = input("Which direction do you want to move? (n/s/e/w/u/d): ")
        if direction == 'n':
            if y > 0 and cavern[z][y-1][x] != '#':
                y -= 1
            else:
                print("You can't move that way.")
        elif direction == 's':
            if y < len(cavern[z])-1 and cavern[z][y+1][x] != '#':
                y += 1
            else:
                print("You can't move that way.")
        elif direction == 'e':
            if x < len(cavern[z][y])-1 and cavern[z][y][x+1] != '#':
                x += 1
            else:
                print("You can't move that way.")
        elif direction == 'w':
            if x > 0 and cavern[z][y][x-1] != '#':
                x -= 1
            else:
                print("You can't move that way.")
        elif direction == 'u':
            if z > 0 and cavern[z-1][y][x] != '#':
                z -= 1
            else:
                print("You can't move that way.")
        elif direction == 'd':
            if z < len(cavern)-1 and cavern[z+1][y][x] != '#':
                z += 1
            else:
                print("You can't move that way.")
        else:
            print("Invalid direction.")

# Create a cavern
cavern = create_cavern(20, 10, 5)

# Explore the cavern
explore_cavern(cavern)