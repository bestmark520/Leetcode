# 274. H-Index Attempted # python

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # 有H篇論文至少被引用H次
        h_score = 0
        for i in range(1, len(citations) + 1):
            count = 0
            for j in citations:
                if j >= i:
                    count += 1
                if count >= i:
                    h_score = max(h_score, i)
        return h_score
# print(Solution.hIndex(Solution,[1]))