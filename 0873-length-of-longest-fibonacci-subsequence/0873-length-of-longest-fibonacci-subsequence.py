class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        hashT, res = set(A), 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                x, y = A[j], A[j]+A[i]
                size = 2
                while y in hashT:
                    x, y = y, x+y
                    size += 1
                res = max(res, size)
        return res if res >= 3 else 0