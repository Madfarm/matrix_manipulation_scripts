def product_except_self(nums):
    length = len(nums)
    answer = [0]*length

    # answer[i] contains the product of all the numbers to the left
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    # R contains the product of all the numbers to the right
    # Note: for the last element, there are no elements to the right,
    # so the R would be 1
    R = 1;
    for i in reversed(range(length)):
        # For the index 'i', R would contain the 
        # product of all numbers to the right. We update R accordingly
        answer[i] = answer[i] * R
        R *= nums[i]

    return answer

print(product_except_self([1,2,3,4]))