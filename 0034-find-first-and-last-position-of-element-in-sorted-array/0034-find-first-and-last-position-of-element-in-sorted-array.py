class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # first in a binary way find the location of target/ then adjust it to find the beg and end
        i, j = 0, len(nums)-1
        while i<=j:
            m = (i+j)//2
            if nums[m]==target:
                im = m
                while im>=0 and nums[im]==target: im-=1
                jm = m
                while jm<len(nums) and nums[jm]==target: jm+=1
                return [im+1, jm-1] 

            elif target>nums[m]: i = m+1
            else: j= m-1
        return [-1, -1]