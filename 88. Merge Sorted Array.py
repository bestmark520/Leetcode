# 88. Merge Sorted Array  # python

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        b = []
        for i in range(m):
            b.append(nums1[i])
        for j in range(n):
            b.append(nums2[j])
        b.sort()
        nums1[:] = b  # 因為題目說最後要看nums1長什麼樣子

        '''
        # GPT的快速解法
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()  # 排序
        '''

        return nums1
