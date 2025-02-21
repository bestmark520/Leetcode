# 27. Remove Element  # python

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        k = len(nums)

        '''
        # GPT提供的方法
        k = 0  # 用來記錄「非 val」的元素應該放置的位置
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # 將「不等於 val」的值移動到 nums[k]
                k += 1  # k 向前移動
        '''

        return k
