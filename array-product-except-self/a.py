def productExceptSelf(nums):
    # Initialize two arrays
    n = len(nums)
    output = [0]*n
    left = [0]*n
    right = [0]*n

    # Initialize the first element of left and right array
    left[0] = 1
    right[n-1] = 1

    # Construct the left array
    for i in range(1, n):
        left[i] = nums[i-1] * left[i-1]

    # Construct the right array
    for i in range(n-2, -1, -1):
        right[i] = nums[i+1] * right[i+1]

    # Construct the output array
    for i in range(n):
        output[i] = left[i] * right[i]

    return output

# Test the function
nums = [1, 2, 3, 4, 5]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]