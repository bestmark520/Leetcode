# 42. Trapping Rain Water # python

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        L2R_up = 0
        R2L_up = 0
        L2R_line = [0]*n
        R2L_line = [0]*n
        result = 0
        result2 = 0

        for i in range(n):
            L2R_up = max(L2R_up, height[i])
            L2R_line[i] = L2R_up
        
        for i in range(n-1,-1,-1):
            R2L_up = max(R2L_up, height[i])
            R2L_line[i] = R2L_up

            result = min(R2L_line[i], L2R_line[i])
            result = result - height[i]
            if result > 0:
                result2 += result
        return result2

