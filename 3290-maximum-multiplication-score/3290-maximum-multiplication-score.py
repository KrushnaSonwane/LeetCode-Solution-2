class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i == 4: return 0
            if j == len(b): return -inf
            res = a[i] * b[j] + dfs(i+1, j+1)
            res = max(res, dfs(i, j+1))
            return res
        return dfs(0, 0)