# 135. Candy Solved # python

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy_L2R = [1] * n
        candy_R2L = [1] * n
        candy_result = [1] * n
        sum = 0
        # 由左到右，跟右邊比，如果比較大就+1，如果一樣就維持1
        for i in range(0, n-1):
            if ratings[i] < ratings[i+1]:
                candy_L2R[i+1] = candy_L2R[i] + 1
        # print(candy_L2R)
        # 由右到左，跟左邊比，如果比較大就+1，如果一樣就維持1
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candy_R2L[j] = candy_R2L[j + 1] + 1
        # print(candy_R2L)
        for k in range(n):
            candy_result[k] = max(candy_L2R[k], candy_R2L[k])
        for i in range(n):
            sum += candy_result[i]
        return sum

# print(Solution.candy(Solution, [0,1,0,2,1,0,1,3,2,1,2,1]))
