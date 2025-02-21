# 238. Product of Array Except Self Solved # python

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        start = 1
        for i in range(0, n - 1, 1):
            start *= nums[i]
            answer[i + 1] *= start
        start = 1
        for i in range(n - 1, 0, -1):
            start *= nums[i]
            answer[i - 1] *= start
        return answer 
