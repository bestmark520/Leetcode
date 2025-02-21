# 42. Trapping Rain Water # python

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        L2R_up = height[0]
        R2L_up = height[n - 1]
        L2R_line = [0] * n
        R2L_line = [0] * n
        result_process1 = 0
        result_process2 = 0
        result = 0

        for i in range(n):
            L2R_up = max(L2R_up, height[i])
            L2R_line[i] = L2R_up

        for i in range(n - 1, -1, -1):
            R2L_up = max(R2L_up, height[i])
            R2L_line[i] = R2L_up
            result_process1 = min(R2L_line[i], L2R_line[i])
            result_process2 = result_process1 - height[i]
            if result_process2 > 0:
                result += result_process2
        return result
