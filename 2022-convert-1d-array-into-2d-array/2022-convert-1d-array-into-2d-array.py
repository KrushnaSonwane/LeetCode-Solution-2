class Solution:
    def construct2DArray(self, A: List[int], m: int, n: int) -> List[List[int]]:
        if len(A) != m*n: return []
        res, i = [], 0
        for _ in range(m):
            t = []
            for _ in range(n):
                t.append(A[i])
                i += 1
            res.append(t)
        return res