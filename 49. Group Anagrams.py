class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            ans[sorted_str].append(s)
        return list(ans.values())
