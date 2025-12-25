# 122. Best Time to Buy and Sell Stock II # python

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 只要明天的價格比今天高，就今天買明天賣
        # GPT說這是Greedy
        max_profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i]<prices[i+1]:
                max_profit = max_profit+(prices[i+1]-prices[i])
        return max_profit

print(Solution.maxProfit(Solution,[7,1,5,3,6,4]))