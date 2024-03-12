def combinationSum2(candidates, target):
    def dfs(candidates, target, start, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(start, len(candidates)):
            # i > start ensures that no duplication of sets in the combination 
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # explore remaining part
            dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)

    candidates.sort()
    res = []
    dfs(candidates, target, 0, [], res)
    return res


# Test the function
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))