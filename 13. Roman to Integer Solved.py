# 13. Roman to Integer Solved # python

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
        }
        sum = s_dict[s[len(s)-1]]
        for i in range(len(s)-1):
            if s_dict[s[i]]< s_dict[s[i+1]]:
                sum -= s_dict[s[i]]
            else:
                sum += s_dict[s[i]]
        return sum