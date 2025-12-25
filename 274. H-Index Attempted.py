# 274. H-Index Attempted # python

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # 最多有H篇論文至少被引用H次
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

class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        count = [0] * (n + 1)

        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1

        total = 0
        for h in range(n, -1, -1):
            total += count[h]
            if total >= h:
                return h
