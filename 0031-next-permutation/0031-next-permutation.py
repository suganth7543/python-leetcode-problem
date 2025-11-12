class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        idx = -1

        # Step 1: Find the pivot
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                idx = i - 1
                break

        # Step 2: Find the rightmost successor and swap
        if idx != -1:
            for i in range(n - 1, idx, -1):
                if nums[i] > nums[idx]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    break

        # Step 3: Reverse the suffix
        self.reverse(nums, idx + 1, n - 1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1