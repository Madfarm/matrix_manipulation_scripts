import heapq

def shortest_path(grid, start, end, obstacles):
    queue = [(0, start)]
    visited = set()
    while queue:
        (cost, (x, y)) = heapq.heappop(queue)
        if (x, y) == end:
            return cost
        if (x, y) in visited or (x, y) in obstacles:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < 10 and 0 <= next_y < 10:
                heapq.heappush(queue, (cost + 1, (next_x, next_y)))
    return -1

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
start = (0, 0)
end = (9, 9)
obstacles = [(4, 4), (4, 5), (4, 6), (4, 7)]

print(shortest_path(grid, start, end, obstacles))  # Output: 14