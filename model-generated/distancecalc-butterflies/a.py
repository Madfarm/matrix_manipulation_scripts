import datetime

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def calculate_time(distance, speed):
    return distance / speed

def simulate_migration(waypoints):
    total_distance = 0
    total_time = datetime.timedelta(0)
    speed = 25  # km/h

    for i in range(len(waypoints) - 1):
        x1, y1 = waypoints[i]
        x2, y2 = waypoints[i + 1]
        distance = calculate_distance(x1, y1, x2, y2)
        total_distance += distance
        time = calculate_time(distance, speed)
        total_time += datetime.timedelta(hours=time)
        print(f'Reach waypoint {i + 1} in {time} hours')

    print(f'Total distance: {total_distance} km')
    print(f'Average speed: {total_distance / (total_time.total_seconds() / 3600)} km/h')
    print(f'Total time: {total_time.total_seconds() / 3600} hours')

# Example waypoints
waypoints = [(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]
simulate_migration(waypoints)