import random


def generate_dna_sequence(length):
    bases = ['A', 'C', 'G', 'T']
    sequence = [random.choice(bases) for _ in range(length)]
    return ''.join(sequence)


def find_longest_common_subsequence(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs))


def mutate_dna(sequence):
    mutation_type = random.choice(['replace', 'delete', 'add'])
    if mutation_type == 'replace':
        position = random.randint(0, len(sequence) - 1)
        bases = ['A', 'C', 'G', 'T']
        bases.remove(sequence[position])
        new_base = random.choice(bases)
        sequence = sequence[:position] + new_base + sequence[position + 1:]
    elif mutation_type == 'delete':
        position = random.randint(0, len(sequence) - 1)
        sequence = sequence[:position] + sequence[position + 1:]
    else:  # add
        position = random.randint(0, len(sequence))
        new_base = random.choice(['A', 'C', 'G', 'T'])
        sequence = sequence[:position] + new_base + sequence[position:]
    return sequence




seq1 = generate_dna_sequence(10)
seq2 = generate_dna_sequence(15)


print("Sequence 1: ", seq1)
print("Sequence 2: ", seq2)




lcs = find_longest_common_subsequence(seq1, seq2)
print("Longest Common Subsequence: ", lcs)




mutated_seq1 = mutate_dna(seq1)
print("Mutated Sequence 1: ", mutated_seq1)