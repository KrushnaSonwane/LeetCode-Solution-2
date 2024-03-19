class Solution:
    def sumOfPower(self, A: List[int], k: int) -> int:
        n, MOD = len(A), 10**9+7
        @cache
        def dfs(i, sum_, size):
            if k == sum_: return 2 ** size
            if sum_ > k or i == len(A): return 0
            return (dfs(i+1, sum_, size) + dfs(i+1, sum_+A[i], size-1)) % MOD
        return dfs(0, 0, n)