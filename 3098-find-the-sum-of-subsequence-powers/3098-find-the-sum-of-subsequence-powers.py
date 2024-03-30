class Solution:
    def sumOfPowers(self, A: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(i, a, diff, k):
            if k == 0:
                return diff
            if i == len(A): 
                return 0
            ans = dp(i+1, A[i], min(diff, abs(a-A[i])), k-1) + dp(i+1, a, diff, k)
            ans %= (10**9+7)
            return ans
        ans = 0
        A.sort()
        for i, num in enumerate(A):
            ans += dp(i+1, A[i], float("inf"), k-1)
        return ans % (10**9+7)
        