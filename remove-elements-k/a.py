def remove_element(nums, val):
    nums[:] = [x for x in nums if x != val]
    return len(nums)

# Test the function
nums = [3,2,2,3]
val = 3
print(remove_element(nums, val))  # Output: 2