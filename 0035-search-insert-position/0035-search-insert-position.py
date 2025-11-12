class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)+1):
            if(i < len(nums)):
                if (nums[i] >= target):
                    return i
            if(i == len(nums)):
                return i
            