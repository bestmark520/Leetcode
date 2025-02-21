# 121. Best Time to Buy and Sell Stock # python

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        # 這個方法會超時
        max_profit = 0
        for i in range(len(prices) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                now_profit = prices[i] - prices[j]
                max_profit = max(max_profit, now_profit)
        '''
        # O(n)，邏輯是有更低的價格再更新就好，否則一路往下更新max_profit
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
