def find_subsets(nums):
    subsets = []
    generate_subsets(nums, 0, [], subsets)
    return subsets

def generate_subsets(nums, index, current, subsets):
    subsets.append(list(current))
    for i in range(index, len(nums)):
        current.append(nums[i])
        generate_subsets(nums, i + 1, current, subsets)
        current.pop()

# Test the function
nums = [1, 2, 3]
print(find_subsets(nums))