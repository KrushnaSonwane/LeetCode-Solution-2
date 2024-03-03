class Solution:
    def countSubmatrices(self, A: List[List[int]], k: int) -> int:
        res, m, n = 0, len(A), len(A[0])
        prefix = [0 for _ in range(m)]
        for j in range(n):
            sum_ = 0
            for i in range(m):
                prefix[i] += A[i][j]
                sum_ += prefix[i]
                res += sum_ <= k
        return res