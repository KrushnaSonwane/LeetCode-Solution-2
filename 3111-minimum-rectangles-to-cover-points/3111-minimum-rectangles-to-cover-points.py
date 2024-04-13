class Solution:
    def minRectanglesToCoverPoints(self, A: List[List[int]], w: int) -> int:
        A.sort()
        res = 1
        last = A[0][0]
        for i in range(len(A)):
            x, y = A[i]
            if x - last <= w:
                continue
            else:
                last = x
                res += 1
        return res