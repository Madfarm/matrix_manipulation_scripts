def calculate_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def plan_route(interstellar_bodies, max_travel_distance):
    unvisited = set(interstellar_bodies.keys()) - {'Earth'}
    current_location = 'Earth'
    route = ['Earth']
    total_distance = 0
    
    while unvisited:
        nearest_neighbor = min(unvisited, key=lambda x: calculate_distance(interstellar_bodies[x], interstellar_bodies[current_location]))
        distance = calculate_distance(interstellar_bodies[nearest_neighbor], interstellar_bodies[current_location])
        if distance > max_travel_distance:
            print(f"Warning: Cannot reach {nearest_neighbor} within a day's travel.")
            unvisited.remove(nearest_neighbor)
            continue # skip to the next nearest 
        
        total_distance += distance
        route.append(nearest_neighbor)
        current_location = nearest_neighbor
        unvisited.remove(nearest_neighbor)
    
    # Return to Earth
    route.append('Earth')
    total_distance+= calculate_distance(interstellar_bodies[current_location], interstellar_bodies['Earth'])
    return route, total_distance

interstellar_bodies = {'Earth': (0, 0), 'Body1': (3, 4), 'Body2': (1, -2)}
max_travel_distance = 5 
route, distance = plan_route(interstellar_bodies, max_travel_distance)
print(route)
print(distance) 