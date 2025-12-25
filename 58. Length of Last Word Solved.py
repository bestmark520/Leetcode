# 58. Length of Last Word Solved # python

class Solution(object):
    def lengthOfLastWord(self, s): # 反面解法
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        for i in range(n - 1, -1, -1):
            if s[i] != ' ':
                count += 1
            elif count != 0:
                return count

        return count

    def lengthOfLastWord2(self, s): # 正面解法
        """
        :type s: str
        :rtype: int
        """
        result = 0
        spare = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if result != 0:
                    spare = result
                result = 0
            else:
                result += 1
        
        if result == 0:
            return spare
        else:
            return result
