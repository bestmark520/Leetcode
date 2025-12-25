# 238. Product of Array Except Self Solved # python

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        left = 1
        for i in range(0, n - 1, 1):
            left *= nums[i] # 因為你要累乘
            answer[i + 1] *= left
        right = 1
        for i in range(n - 1, 0, -1):
            right *= nums[i]
            answer[i - 1] *= right
        return answer 