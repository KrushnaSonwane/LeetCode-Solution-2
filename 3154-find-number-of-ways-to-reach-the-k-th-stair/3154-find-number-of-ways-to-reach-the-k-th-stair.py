class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(pos, jump, last):
            if pos > k+1: return 0
            res = 1 if pos == k else 0
            if last:
                res += dfs(pos + 2 ** jump, jump +1, False)
            else:
                res += dfs(pos - 1, jump, True)
                res += dfs(pos + 2 ** jump, jump+1, False)
            return res
        return dfs(1, 0, False)