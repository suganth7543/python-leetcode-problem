class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                total = 0
                return
            if total > target:
                total = 0
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                #total += candidates[i]
                backtrack(i, path, total+candidates[i])
                path.pop()
        backtrack(start = 0, path=[], total = 0)
        return res
