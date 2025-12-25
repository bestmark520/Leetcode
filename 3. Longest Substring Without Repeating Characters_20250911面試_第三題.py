class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        seen = {}
        start = 0
        count = 0
        max_len = 0

        for i in range(n):
            if s[i] in seen and seen[s[i]] >= start:
                start = seen[s[i]] + 1 # 如dvdf，遇到第二個d起點從v開始
                count = i - start # count不見得會直接歸0，
                # 例如dvdf，遇到第二個d時，count = 2-1 = 1，
                # 後面馬上count += 1，count = 2，count會從v開始算
            seen[s[i]] = i # 把s字串加入到字典，seen[s[0]] = 0 →seen = {'a': 0}
            count += 1
            if count > max_len:
                max_len = count
                results = s[start:i+1] # 字串切割範圍從start到i+1-1
        return results

solution = Solution()
print(solution.lengthOfLongestSubstring("abbcdef"))
