class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []

        if len(nums) == 1:
            return 1

        for indx in range(len(nums) - 1):
            if indx == 0: 
               lst.append(nums[indx])

            if nums[indx] != nums[indx + 1]:
                lst.append(nums[indx + 1])
        nums[:] = lst
        return len(nums)

