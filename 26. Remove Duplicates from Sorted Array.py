# 26. Remove Duplicates from Sorted Array # python

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        error = []

        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] == nums[i]:
                error.append(i)
        
        for j in error:
            del nums[j]

        k = len(nums)
        
        return k
