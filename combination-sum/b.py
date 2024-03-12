def combination_sum(candidates, target):
    def dfs(candidates, target, start, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(start, len(candidates)):
            dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)
    
    res = []
    dfs(candidates, target, 0, [], res)
    return res

# Testing the function
candidates = [2,3,6,7]
target = 7
print(combination_sum(candidates, target))