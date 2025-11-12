class Solution(object):
    def combinationSum2(self, candidates, target):
        # O(2^n)
        # O(n)
        output = []
        candidates.sort()
        def backtract(i, path, pathSum):
            if pathSum == target:
                output.append(list(path))
                return
            
            prev = -1
            for j in range(i, len(candidates)):
                if pathSum + candidates[j] > target or candidates[j] == prev:
                    continue
                    
                backtract(j + 1, path + [candidates[j]], pathSum + candidates[j])
                prev = candidates[j]
            
        backtract(0, [], 0)

        return output