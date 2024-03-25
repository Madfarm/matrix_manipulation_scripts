def balanced_substrings(s):
    count = 0
    balance = 0
    for char in s:
        balance += 1 if char == 'L' else -1
        if balance == 0:
            count += 1
    return count

print(balanced_substrings('LLRR'))  # Output: 1
print(balanced_substrings('LLLRRR'))  # Output: 1
print(balanced_substrings('LLLRRRLR'))  # Output: 2
print(balanced_substrings('LLL'))  # Output: 0
print(balanced_substrings('RR'))  # Output: 0
print(balanced_substrings('LR'))  # Output: 1
print(balanced_substrings(''))  # Output: 0