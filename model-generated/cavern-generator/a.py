import random

class Room:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.visited = False
        self.walls = [True, True, True, True]  # Top, Right, Bottom, Left

class Cavern:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.rooms = [[[Room(x, y, z) for z in range(depth)] for y in range(height)] for x in range(width)]

    def generate_cavern(self):
        for x in range(self.width):
            for y in range(self.height):
                for z in range(self.depth):
                    room = self.rooms[x][y][z]
                    if x == 0:
                        room.walls[3] = False
                    elif x == self.width - 1:
                        room.walls[1] = False
                    else:
                        if random.random() < 0.5:
                            room.walls[3] = False
                            self.rooms[x - 1][y][z].walls[1] = False
                    if y == 0:
                        room.walls[0] = False
                    elif y == self.height - 1:
                        room.walls[2] = False
                    else:
                        if random.random() < 0.5:
                            room.walls[0] = False
                            self.rooms[x][y - 1][z].walls[2] = False
                    if z == 0:
                        room.walls[0] = False
                    elif z == self.depth - 1:
                        room.walls[2] = False
                    else:
                        if random.random() < 0.5:
                            room.walls[0] = False
                            self.rooms[x][y][z - 1].walls[2] = False

    def print_cavern(self):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    room = self.rooms[x][y][z]
                    if room.walls[0]:
                        print("###", end="")
                    else:
                        print("   ", end="")
                    if room.walls[1]:
                        print("###", end="")
                    else:
                        print("   ", end="")
                print()
            print()

cavern = Cavern(10, 5, 3)
cavern.generate_cavern()
cavern.print_cavern()