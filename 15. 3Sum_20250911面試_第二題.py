class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        Target = 0

        for i in range(n):  # 以第i個數字為主角，再去看右邊的範圍有沒有可以配合的兩個數字
            if i > 0 and nums[i] == nums[i-1]:  # 如果跟上一個數字一樣，就跳過不重複做
                continue
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == Target:
                    ans.append([nums[i], nums[left], nums[right]]) # List[List[int]]的方法
                    while left < right and nums[left] == nums[left+1]:
                        left += 1 # 避免重複算
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1 # 避免重複算

                    left += 1
                    right -= 1

                elif total < Target:
                    left += 1 # 如果太小就左邊+1，因為有sort過左邊是小的
                else:
                    right -= 1 # 如果太大就右邊-1，因為sort過右邊是大的
        return ans

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
