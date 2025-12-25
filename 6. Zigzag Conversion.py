# 6. Zigzag Conversion # python

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row = numRows
        n = len(s)
        ans_ = [""] * row  # 可以把值存到ans_[0]、ans_[1] ...
        cycle = row + row - 2
        if cycle == 0:
            return s

        for i in range(n):
            x = i % cycle
            if x >= row:
                x = cycle - x
            ans_[x] += s[i] if 0 <= x < numRows else ""

        return "".join(ans_)

'''
N = 3 一個穿插：
1   5   9     13
2 4 6 8 10 12 14
3   7   11

1   1   1   
2 4 2 4 2 4
3   3   3

N = 4 兩個穿插：

1     7      13
2   6 8   12 14
3 5   9 11   
4     10     

1     1    1    1
2   6 2  6 2  6 2
3 5   3 5  3 5 
4     4    4


'''