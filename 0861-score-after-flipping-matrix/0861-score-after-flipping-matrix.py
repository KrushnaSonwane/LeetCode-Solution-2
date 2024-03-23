class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        hashT = Counter()
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 0 if A[i][j] else 1
        for i in range(m):
            for j in range(n):
                hashT[j] += A[i][j]
        res, count = 0, n-1
        for j in range(n):
            if m - hashT[j] > hashT[j]:
                for i in range(m):
                    A[i][j] = 0 if A[i][j] else 1
            for i in range(m):
                if A[i][j]:
                    res += 2 ** count
            count -= 1
        return res