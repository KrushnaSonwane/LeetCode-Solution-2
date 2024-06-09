class Solution:
    def maxTotalReward(self, A: List[int]) -> int:
        A = sorted(list(set(A)))
        dp = {}
        def dfs(i, sum_):
            if sum_ >= 2000 or i == len(A): return 0
            if (i, sum_) in dp: return dp[(i, sum_)]
            res = dfs(i+1, sum_)
            if A[i] > sum_:
                res = max(res, dfs(i+1, sum_+A[i]) + A[i])
            dp[(i, sum_)] = res
            return res
        return dfs(0, 0)