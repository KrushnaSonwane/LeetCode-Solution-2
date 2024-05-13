class Solution:
    def maximumEnergy(self, A: List[int], k: int) -> int:
        @cache
        def dfs(i, start):
            if i >= len(A): return -inf if not start else 0
            res = -inf
            if not start:
                res = max(res, dfs(i+1, 0))
            res = max(res, dfs(i+k, 1) + A[i])
            return res
        return dfs(0, 0)