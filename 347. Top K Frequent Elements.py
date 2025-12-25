class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dict1 = {}
        for n in nums:
            dict1[n] = dict1.get(n, 0) + 1

        list1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in list1[:k]]
        return result