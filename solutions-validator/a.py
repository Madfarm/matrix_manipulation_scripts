def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "()" in code:
        return "missing param"
    if code.count("    ") < 2:  # 4 spaces for indentation
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True

# Test the function with itself
print(validate(validate.__code__.co_code.decode()))