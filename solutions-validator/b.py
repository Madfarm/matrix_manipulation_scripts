def validate(code):
    checks = [
        ("def", "missing def"),
        (":", "missing :"),
        ("(", "missing paren"),
        (")", "missing paren"),
        ("    ", "missing indent"),
        ("validate", "wrong name"),
        ("return", "missing return"),
    ]
    
    for check in checks:
        if check[0] not in code:
            return check[1]
    
    return True

code = """
def validate(code):
    checks = [
        ("def", "missing def"),
        (":", "missing :"),
        ("(", "missing paren"),
        (")", "missing paren"),
        ("    ", "missing indent"),
        ("validate", "wrong name"),
        ("return", "missing return"),
    ]
    
    for check in checks:
        if check[0] not in code:
            return check[1]
    
    return True
"""

print(validate(code))

