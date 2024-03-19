import sys

def MMSum(a, b, c, d, e):
    nums = [a, b, c, d, e]
    nums.sort()
    min_sum = sum(nums[:4])
    max_sum = sum(nums[1:])
    return min_sum, max_sum

min_sum, max_sum = MMSum(1, 2, 3, 4, 5)
sys.stdout.write("{} {}\n".format(min_sum, max_sum))