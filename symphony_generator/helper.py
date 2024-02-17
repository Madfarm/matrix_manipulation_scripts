import random

def generate_symphony_codeB():
    # Generate three groups of 4 characters separated by hyphens
    code = []
    for i in range(3):
        group = []
        for j in range(4):
            # print(group)
            group.append(random.choice(["A", "B", "C", "D", "E", "F", "G"]))
        code.append("".join(group))

        print(code)
    return "-".join(code)

print(generate_symphony_codeB())


def generate_symphony_codeA():
    # Generate three groups of 4 characters separated by hyphens
    code = []
    for i in range(3):
        group = []
        for j in range(4):
            group.append(random.choice(["A", "B", "C", "D", "E", "F", "G"]))
        code.append("".join(group))
    return "-".join(code)

print(generate_symphony_codeA())


