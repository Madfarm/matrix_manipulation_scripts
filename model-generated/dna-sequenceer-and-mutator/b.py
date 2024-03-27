import random


def generate_dna(length):
    bases = ['A', 'C', 'G', 'T']
    return ''.join(random.choice(bases) for _ in range(length))


def longest_common_subsequence(dna1, dna2):
    m, n = len(dna1), len(dna2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i - 1] == dna2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if dna1[i - 1] == dna2[j - 1]:
            lcs.append(dna1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs))


def difference(dna1, dna2):
    return sum(base1 != base2 for base1, base2 in zip(dna1, dna2))


def mutate(dna):
    mutated_dna = list(dna)
    for i in range(len(dna)):
        if random.random() < 0.1:
            if random.random() < 0.5:
                mutated_dna[i] = random.choice(['A', 'C', 'G', 'T'])
            else:
                if random.random() < 0.5:
                    del mutated_dna[i]
                else:
                    mutated_dna.insert(i, random.choice(['A', 'C', 'G', 'T']))
    return ''.join(mutated_dna)


dna1 = generate_dna(10)
dna2 = generate_dna(10)


lcs = longest_common_subsequence(dna1, dna2)


diff = difference(dna1, dna2)


mutated_dna = mutate(dna1)

print(f"DNA 1: {dna1}")
print(f"DNA 2: {dna2}")
print(f"Longest Common Subsequence: {lcs}")
print(f"Difference: {diff}")
print(f"Mutated DNA: {mutated_dna}")