import math

def pyramid_builder():
    # Get user input
    total_blocks = int(input("Enter the total number of blocks: "))
    num_builders = int(input("Enter the number of builders: "))
    block_ratio = float(input("Enter the block ratio (0-1): "))
    time_per_block = int(input("Enter the time per block (in seconds): "))

    # Initialize variables
    height = 0
    time = 0
    leftover_blocks = total_blocks

    # Loop until all blocks are used
    while leftover_blocks >= (height + 1) * num_builders:
        height += 1
        blocks_needed = (height + 1) * num_builders
        time_required_for_layer = blocks_needed * time_per_block / num_builders
        time += time_required_for_layer
        leftover_blocks -= blocks_needed

        # Reduce the number of blocks for the next layer based on the reduction ratio
        leftover_blocks *= block_ratio

    # Calculate the maximum height of the pyramid
    max_height = height

    # Calculate the total time required to build the pyramid
    total_time = time

    # Calculate the leftover blocks
    leftover_blocks = leftover_blocks

    # Print the results
    print("Maximum height of the pyramid:", max_height)
    print("Total time required to build the pyramid:", total_time)
    print("Leftover blocks:", leftover_blocks)

# Call the function
pyramid_builder()