# 28. Find the Index of the First Occurrence in a String # python

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        answer = []
        for i in range(0, len(haystack)):
            count = 0
            for j in range(i, len(haystack)):
                if haystack[j] == needle[count]:
                    count += 1
                elif haystack[j] != needle[count]:
                    count = 0
                if count == len(needle):
                    x = j-count+1
                    answer.append(x)
                    count = 0
        if answer != []:
            return min(answer)
        return -1
