import pandas as pd
import random


def random_walk(steps):
    # Assertion to check if the input is a positive integer
    assert isinstance(steps, int) and steps > 0, "Input should be a positive integer"


    # Initialize the position at 0
    position = 0


    # Initialize lists to store the step numbers and positions
    step_numbers = []
    positions = []


    # Simulate the random walk
    for step in range(steps):
        # Assertion to check if the step number is correct
        assert step == len(step_numbers), "Incorrect step number"


        # Append the current step number and position
        step_numbers.append(step)
        positions.append(position)


        # Move up or down with equal probability
        move = random.choice([-1, 1])
        position += move


    # Create a DataFrame
    df = pd.DataFrame({'Step': step_numbers, 'Position': positions})


    # Assertion to check if the DataFrame has the correct shape
    assert df.shape == (steps, 2), "Incorrect DataFrame shape"


    return df


# Test the function
print(random_walk(10))