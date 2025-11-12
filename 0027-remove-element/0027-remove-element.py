class Solution(object):
    def removeElement(self, nums, val):
       n=[x for x in nums if x!=val]
       l=len(n)
       for i in range(l):
        nums[i]=n[i]
       return l
        
        