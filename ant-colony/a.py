import random

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Anthill:
    def __init__(self, size):
        self.size = size
        self.grid = [['ground' for _ in range(size)] for _ in range(size)]
        self.ants = []
        self.queen = Ant(random.randint(0, size-1), random.randint(0, size-1))
        self.grid[self.queen.x][self.queen.y] = 'queen'

    def add_ant(self):
        x = random.randint(0, self.size-1)
        y = random.randint(0, self.size-1)
        if self.grid[x][y] == 'ground':
            self.ants.append(Ant(x, y))
            self.grid[x][y] = 'ant'

    def move_ant(self, ant):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = random.choice(directions)
        new_x, new_y = ant.x + dx, ant.y + dy
        if 0 <= new_x < self.size and 0 <= new_y < self.size and self.grid[new_x][new_y] == 'ground':
            self.grid[ant.x][ant.y] = 'ground'
            ant.x, ant.y = new_x, new_y
            self.grid[ant.x][ant.y] = 'ant'

    def tunnel(self, ant):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = random.choice(directions)
        new_x, new_y = ant.x + dx, ant.y + dy
        if 0 <= new_x < self.size and 0 <= new_y < self.size and self.grid[new_x][new_y] == 'ground':
            self.grid[new_x][new_y] = 'tunnel'

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()

def simulate(size, num_ants, steps):
    anthill = Anthill(size)
    for _ in range(num_ants):
        anthill.add_ant()

    for _ in range(steps):
        for ant in anthill.ants:
            anthill.move_ant(ant)
            anthill.tunnel(ant)
        anthill.print_grid()

simulate(10, 10, 10)