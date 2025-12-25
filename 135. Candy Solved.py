# 135. Candy Solved # python

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy_L2R = [1]*n
        candy_R2L = [1]*n
        candy_result = [1]*n
        sum = 0
        for i in range(1, n):
            if ratings[i]>ratings[i-1]: candy_L2R[i] = candy_L2R[i-1]+1
        for j in range(n-2, -1, -1):
            if ratings[j]>ratings[j+1]: candy_R2L[j] = candy_R2L[j+1]+1
        for k in range(n):
            candy_result[k] = max(candy_L2R[k], candy_R2L[k])
            
            sum += candy_result[k]
        return sum
