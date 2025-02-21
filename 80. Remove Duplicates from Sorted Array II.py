# 80. Remove Duplicates from Sorted Array II # python

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 1:
                    del nums[i]
            else:
                count = 0

        k = len(nums)
        return k