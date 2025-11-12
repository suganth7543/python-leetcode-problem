class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        if n == 1:
            return nums

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        def bs(start, end, k):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > k:
                    start = mid + 1
                else:
                    end = mid - 1
            return start - 1

        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                j = bs(i + 1, n - 1, nums[i])
                nums[i], nums[j] = nums[j], nums[i]
                reverse(i + 1, n - 1)
                return nums
            else:
                i -= 1

        reverse(0, n - 1)
        return nums