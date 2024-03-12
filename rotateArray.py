def rotate(nums, k):
    k = k % len(nums)  # In case k is larger than the length of the array
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Test the function
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))  # Output: [5, 6, 7, 1, 2, 3, 4]