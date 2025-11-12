class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        def dfs(i, path, total):
            if target == total:
                res.append(list(path))
                return
        
            for j in range(i, len(candidates)):
                if target >= candidates[j] + total:
                    dfs(j, path + [candidates[j]], total + candidates[j])

        dfs(0, [], 0)

        return res