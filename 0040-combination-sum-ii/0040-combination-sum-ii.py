class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # sort to help skip duplicates
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(list(path))
                return
            if total > target:
                return
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # skip duplicates
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # move to next index
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return result
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]