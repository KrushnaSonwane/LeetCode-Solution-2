class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        @cache
        def dfs(i, last):
            if i == len(A): return 0
            res = inf
            for j in range(len(A[i])):
                if last == j: continue
                res = min(res, dfs(i+1, j) + A[i][j])
            return res
        return dfs(0, -1)