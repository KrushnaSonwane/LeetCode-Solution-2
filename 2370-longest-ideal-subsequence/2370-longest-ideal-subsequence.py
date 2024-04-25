class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp, res = {}, 0
        for i in range(97, 123):
            dp[chr(i)] = 0
        for ch in s:
            res = 0
            for cc in dp:
                if abs(ord(ch)-ord(cc)) <= k:
                    res = max(dp[cc]+1, res)
            dp[ch] = max(res, dp[ch])
        return max(dp.values())    
        