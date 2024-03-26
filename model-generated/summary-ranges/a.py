def summary_ranges(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [f'{nums[0]}']
        
    result = []
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            if start == nums[i-1]:
                result.append(f'{start}')
            else:
                result.append(f'{start}->{nums[i-1]}')
            start = nums[i]
    if start == nums[-1]:
        result.append(f'{start}')
    else:
        result.append(f'{start}->{nums[-1]}')
    return result

print(summary_ranges([0,1,2,4,5,7]))