class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i, j, last):
            if i >= j: return 0
            res = max(dfs(i+1, j, last), dfs(i, j-1, last))
            if s[i] == s[j] != last:
                res = max(res, dfs(i+1, j-1, s[i]) + 2)
            return res
        res = dfs(0, len(s)-1, '')
        dfs.cache_clear()
        return res