def generate_parentheses(n):
    def generate(p, left, right, parens=[]):
        if left: generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right: parens.append(p)
        return parens
    return generate('', n, n)

# Test the function
n = 3
print(generate_parentheses(n))

