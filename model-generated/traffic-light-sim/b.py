import numpy as np


def update_traffic_lights(traffic_lights):
    # Define the order of traffic light states
    order = ["red", "green", "yellow"]


    # For each traffic light in the array
    for i in range(len(traffic_lights)):
        # Get the index of the current state
        current_state = traffic_lights[i]
        current_index = order.index(current_state)


        # Update the state to the next one in the order
        next_index = (current_index + 1) % len(order)
        traffic_lights[i] = order[next_index]


    return traffic_lights


# Initialize the traffic lights
traffic_lights = np.array(["red", "red", "red", "green"])


# Print the initial state
print("Initial state:")
print(traffic_lights)


# Update the traffic lights and print the new state
traffic_lights = update_traffic_lights(traffic_lights)
print("Updated state:")
print(traffic_lights)


# Ensure that the traffic lights are following the sequence
assert np.all(traffic_lights == np.array(["green", "green", "green", "yellow"])), "Traffic lights are not following the sequence"