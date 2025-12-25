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

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2: return len(nums)
        k = 2  # 下一個能放的位置
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k