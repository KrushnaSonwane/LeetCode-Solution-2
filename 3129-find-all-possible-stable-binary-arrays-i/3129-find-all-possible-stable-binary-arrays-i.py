class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i, j, last):
            if i == 0 and j == 0: return 1
            res = 0
            if last == 1:
                for k in range(min(limit, i)):
                    res += dfs(i-(k+1), j, 0)
            else:
                for k in range(min(limit, j)):
                    res += dfs(i, j-(k+1), 1)
            return res % MOD
        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD