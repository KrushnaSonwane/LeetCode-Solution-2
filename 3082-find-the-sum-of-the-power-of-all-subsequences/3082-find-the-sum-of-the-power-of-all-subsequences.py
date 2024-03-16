class Solution:
    def sumOfPower(self, A: List[int], k: int) -> int:
        n, MOD = len(A), 10**9+7
        @cache
        def dfs(i, sum_, size):
            if sum_ == k:
                key = n-size
                return 2**key
            if sum_ > k: return 0
            if i == len(A): return 0
            res = dfs(i+1, sum_, size) % MOD
            res = (res + dfs(i+1, sum_+A[i], size+1)) % MOD
            return res
        return dfs(0, 0, 0)