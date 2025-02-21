# 134. Gas Station # python

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # gas是你抵達時得到的gas
        # cost是你離開時消耗的gas
        # 只要total_gas >= total_cost 就一定有解
        total_tank = 0
        current_tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            # 若目前的油量不足，重新選擇起點
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0  # 重置當前油量 # 不用重置total

        if total_tank >= 0:
            return start_index
        else:
            return -1
