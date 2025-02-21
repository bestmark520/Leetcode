# 55. Jump Game # python

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 假如第一個數字是0就不用跳了
        # 同理nums[n]如果n-1項是0且n-1前面其他項都跳不過來，那n就是死路
        # GPT說這是Greedy
        max_range = nums[0]
        for i in range(len(nums)):
            if i<=max_range:
                max_range = max(max_range, i+nums[i])
            else:
                return False
        return True
