class Solution(object):
    def searchRange(self, nums, target):
        min=0
        max=0
        if target in nums:
            for i in range(0,len(nums)):
                if(nums[i]==target):
                    min=i
                    break
            for j in range(len(nums)-1,-1,-1):
                if(nums[j]==target):
                    max=j
                    break
            return [min,max]
        else:
            return [-1,-1]

        