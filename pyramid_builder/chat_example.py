def build_pyramid(total_blocks, num_builders, reduction_ratio, time_per_block):
    height = 0
    total_time_required = 0
    leftover_blocks = total_blocks

    while leftover_blocks >= (height + 1) * num_builders:
        height += 1
        blocks_needed = (height + 1) * num_builders
        time_required_for_layer = blocks_needed * time_per_block / num_builders
        total_time_required += time_required_for_layer
        leftover_blocks -= blocks_needed

        # Reduce the number of blocks for the next layer based on the reduction ratio
        leftover_blocks *= reduction_ratio

    return height, total_time_required, leftover_blocks

# Example usage:
total_blocks_input = int(input("Enter the total number of blocks: "))
num_builders_input = int(input("Enter the number of builders: "))
reduction_ratio_input = float(input("Enter the reduction ratio for each layer: "))
time_per_block_input = float(input("Enter the time required per block (in units): "))

height, total_time_required, leftover_blocks = build_pyramid(total_blocks_input, num_builders_input, reduction_ratio_input, time_per_block_input)

print(f"Maximum Height of Pyramid: {height}")
print(f"Total Time Required: {total_time_required} units")
print(f"Leftover Blocks: {leftover_blocks}")