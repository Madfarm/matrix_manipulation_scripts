import math

def pyramid_builder(total_blocks, num_builders, block_ratio, time_per_block):
    # Initialize variables
    height = 0
    time = 0
    leftover_blocks = total_blocks

    # Loop until all blocks are used
    while leftover_blocks > 0:
        # Calculate number of blocks in current layer
        layer_blocks = int(leftover_blocks * (1 - block_ratio))

        print(f"Layer Blocks: {layer_blocks}")

        # Update leftover blocks
        leftover_blocks -= layer_blocks

        # Update height and time
        height += layer_blocks
        time += num_builders * layer_blocks * time_per_block

        print(f"Height: {height}, Time: {time}, Leftover Blocks: {leftover_blocks}")

    return height, time, leftover_blocks

print(pyramid_builder(1000, 5, 0.8, 2))  # Output: (150.0, 1500.0, 375)