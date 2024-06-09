class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9+7
        A = [1 for _ in range(n)]
        for _ in range(k):
            last = 0
            for i in range(n):
                A[i] = (A[i]+last) % MOD
                last = A[i]
        return A[i]