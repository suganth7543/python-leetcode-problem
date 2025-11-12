def verif(nums):
    i=0
    while(i<len(nums) and 0<=nums[i]<=50):
        i+=1
    return i==len(nums)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        s=0
        if(0<=len(nums)<=100 and 0<=val<=100 and verif(nums)):
            i=0
            while (i<len(nums)):
                if(nums[i]==val):
                    nums.remove(nums[i])
                else:
                    i+=1
        return len(nums)
        