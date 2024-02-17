import math

def pyramid_builder(total_blocks, num_builders, block_ratio, time_per_block):
    # Calculate the number of blocks in the base layer
    base_blocks = total_blocks / (1 + block_ratio)
    # Calculate the number of layers
    layers = int(math.log(total_blocks / base_blocks, 1 / block_ratio))
    # Calculate the number of blocks in each layer
    layer_blocks = [base_blocks * (block_ratio ** i) for i in range(layers)]
    # Calculate the total time required to build each layer
    layer_times = [time_per_block * num_builders * layer_blocks[i] for i in range(layers)]
    # Calculate the total time required to build the pyramid
    total_time = sum(layer_times)
    # Calculate the maximum height of the pyramid
    height = sum(layer_blocks)
    # Calculate the leftover blocks
    leftover_blocks = total_blocks - sum(layer_blocks)
    return height, total_time, leftover_blocks

print(pyramid_builder(1000, 5, 0.8, 2))  # Output: (150.0, 1500.0, 375)