class Solution:
    def numberOfRightTriangles(self, A: List[List[int]]) -> int:
        row, col = Counter(), Counter()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        res = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    res += (row[i]-1) * (col[j]-1)
        return res