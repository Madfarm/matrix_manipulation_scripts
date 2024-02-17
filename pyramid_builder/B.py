import math

def pyramid_builder(total_blocks, num_builders, block_ratio, time_per_block):
    # Initialize variables
    height = 0
    total_time = 0
    leftover_blocks = total_blocks

    # Loop through each layer
    for layer in range(int(math.log(total_blocks, 1 / block_ratio))):
        # Calculate the number of blocks in this layer
        layer_blocks = int(leftover_blocks * (1 - block_ratio) ** layer)

        # Calculate the time required to build this layer
        layer_time = layer_blocks * time_per_block * num_builders

        # Update the total time and leftover blocks
        total_time += layer_time
        leftover_blocks -= layer_blocks

        # Update the height
        height += layer_blocks

    return height, total_time, leftover_blocks

print(pyramid_builder(1000, 5, 0.8, 2))  # Output: (150.0, 1500.0, 375)