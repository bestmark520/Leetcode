# 169. Majority Element # python

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        max_count = 0
        max_number = nums[0]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count += 1
                if count > max_count:
                    max_number = nums[i]
                max_count = max(max_count,count)
            else:
                count = 0
        return max_number
