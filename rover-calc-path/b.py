class MarsRover:
    def __init__(self, start, dest, obstacles):
        self.start = start
        self.dest = dest
        self.obstacles = obstacles
        self.grid = [[0 for _ in range(10)] for _ in range(10)]
        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[1]] = 1
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.reverse = {0:2, 1:3, 2:0, 3:1}

    def is_valid(self, x, y):
        return 0 <= x < 10 and 0 <= y < 10 and self.grid[x][y] == 0

    def solve(self):
        queue = [(self.start, [])]
        while queue:
            (x, y), path = queue.pop(0)
            if (x, y) == self.dest:
                return path
            for i, (dx, dy) in enumerate(self.moves):
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny):
                    queue.append(((nx, ny), path + [i]))
                    self.grid[nx][ny] = 1
            if path:
                x, y = self.start
                for i in path:
                    nx, ny = x + self.moves[self.reverse[i]][0], y + self.moves[self.reverse[i]][1]
                    if self.is_valid(nx, ny):
                        x, y = nx, ny
                        self.grid[x][y] = 0
        return "No path found"

# Test the program
rover = MarsRover((0, 0), (9, 9), [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)])
print(rover.solve())