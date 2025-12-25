# 189. Rotate Array # python

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n # 處理 k > n 的情況

        nums.reverse()
        nums[:k] = reversed(nums[:k]) # 0~k
        nums[k:] = reversed(nums[k:]) # k~最後
