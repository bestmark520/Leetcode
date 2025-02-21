# 189. Rotate Array # python

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while len(nums)<k:
            k = k-len(nums)
        nums1 = []
        for i in range(len(nums)-1-k+1,len(nums),1):
            nums1.append(nums[i])
        for j in range(0,len(nums)-1-k+1,1):
            nums1.append(nums[j])
        nums[:] = nums1
        return nums