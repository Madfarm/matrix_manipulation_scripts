def largest_common_substring(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0
    max_end = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if i and j and str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    max_end = i
    return str1[max_end - max_length: max_end]

str1 = "abcabcabc"
str2 = "abcabc"
print(largest_common_substring(str1, str2))  # Output: "abcabc"