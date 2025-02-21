# 122. Best Time to Buy and Sell Stock II # python

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        # 這是錯的
        max_profit_list = []
        while len(prices) != 0:
            max_profit = 0
            min_price = prices[0]
            max_place = 0
            i = -1
            for price in prices:
                i = i + 1
                print(i)
                if price < min_price:
                    min_price = price
                else:
                    if price - min_price > max_profit:
                        max_place = i
                    max_profit = max(max_profit, price - min_price)
            max_profit_list.append(max_profit)
            del prices[0:max_place+1]
            print(f"prices:{prices}")
            print(f"max_profit_list:{max_profit_list}")
            print(f"max_place:{max_place}")
            print(f"max_profit:{max_profit}")
            print(f"min_price:{min_price}")
            print()
        max_profit = 0
        for j in max_profit_list:
            max_profit = max_profit + j

        return max_profit
        '''
        # 邏輯是只要今天的價格比昨天高，就當作昨天有買今天賣
        # GPT說這是Greedy # 只用一個for遍佈nums的都是Greedy?
        max_profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i]<prices[i+1]:
                max_profit = max_profit+(prices[i+1]-prices[i])
        return max_profit
print(Solution.maxProfit(Solution,[7,1,5,3,6,4]))