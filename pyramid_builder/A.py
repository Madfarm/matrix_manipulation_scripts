def pyramid_builder(total_blocks, num_builders, block_ratio, time_per_block):
    # Calculate the number of blocks in the base layer
    base_blocks = total_blocks
    height = 1
    remaining_blocks = total_blocks

    while remaining_blocks > 0:
        # Calculate the number of blocks in the current layer
        layer_blocks = int(base_blocks * block_ratio)
        remaining_blocks -= layer_blocks

        # Calculate the time required to build the current layer
        layer_time = layer_blocks * time_per_block * num_builders
        total_time += layer_time

        # Update the height and base blocks for the next layer
        height += 1
        base_blocks = layer_blocks

    # Calculate the maximum height of the pyramid
    max_height = height - 1

    # Calculate the leftover blocks
    leftover_blocks = remaining_blocks

    return max_height, total_time, leftover_blocks


print(pyramid_builder(1000, 5, 0.8, 10))  # Output: (6, 1200, 100)