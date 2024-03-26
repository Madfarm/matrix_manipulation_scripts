def word_puzzle(start, end, words):
    if len(start) != len(end):
        return "Start and end words must be the same length."

    if start not in words or end not in words:
        return "Start or end word is not a valid word."

    puzzle = [start]
    while puzzle[-1] != end:
        for i in range(len(start)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                new_word = puzzle[-1][:i] + letter + puzzle[-1][i+1:]
                if new_word in words and new_word not in puzzle:
                    puzzle.append(new_word)
                    break
            else:
                continue
            break
        else:
            return "No puzzle solution found."

    return puzzle

# Test the function
start_word = "cat"
end_word = "dog"
words = ["cat", "bat", "dog", "log"]
print(word_puzzle(start_word, end_word, words))