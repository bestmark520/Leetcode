# 26. Remove Duplicates from Sorted Array # python

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        k = 1  # 下一個不重複數字要放的位置
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # in-place 覆寫
                k += 1

        return k
