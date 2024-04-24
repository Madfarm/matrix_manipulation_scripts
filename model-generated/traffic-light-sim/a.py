import numpy as np


def update_traffic_light(traffic_lights):
    # Define the state transition rules
    rules = {
        "red": "green",
        "green": "yellow",
        "yellow": "red"
    }


    # Apply the rules to update the traffic lights
    updated_lights = np.array([rules[light] for light in traffic_lights])


    return updated_lights


# Initial state of the traffic lights
traffic_lights = np.array(["red", "red", "red", "green"])


# Update the traffic lights
updated_lights = update_traffic_light(traffic_lights)


# Assert that the lights are following the predefined sequence
assert np.all(updated_lights == np.array(["green", "green", "green", "yellow"])), "Traffic lights are not following the sequence"

