class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        dp = [[0 for _ in s] for _ in s]
        for i in range(len(s)):
            hashT, max_ = Counter(), Counter()
            mx = 0
            for j in range(i, len(s)):
                hashT[s[j]] += 1
                mx = max(mx, hashT[s[j]])
                max_[hashT[s[j]]] += 1
                if max_[mx] == len(hashT):
                    dp[i][j] = 1
        
        @cache
        def dfs(i):
            if i == len(s): return 0
            res = inf
            for j in range(i, len(s)):
                if dp[i][j]:
                    res = min(res, dfs(j+1) + 1)
            return res
        return dfs(0)
        