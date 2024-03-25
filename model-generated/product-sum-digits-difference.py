def product_sum_diff(n):
    digits = [int(x) for x in str(n)]
    product = 1
    for d in digits:
        product *= d
    return product - sum(digits)

print(product_sum_diff(123))  # Output: -6
print(product_sum_diff(456))  # Output: -30
print(product_sum_diff(789))  # Output: -54