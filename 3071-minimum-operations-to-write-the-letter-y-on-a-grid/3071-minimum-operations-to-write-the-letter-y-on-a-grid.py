class Solution:
    def minimumOperationsToWriteY(self, A: List[List[int]]) -> int:
        n = len(A)
        yCount, remCount = [0, 0, 0], [0, 0, 0]
        x, y = 0, 0
        visit = set()
        for _ in range(n//2):
            visit.add((x, y))
            yCount[A[x][y]] += 1
            y += 1
            x += 1
        x, y = 0, n-1
        for _ in range(n//2):
            visit.add((x, y))
            yCount[A[x][y]] += 1
            y -= 1
            x += 1
        x, y = n-1, n//2
        for _ in range(n//2+1):
            visit.add((x, y))
            yCount[A[x][y]] += 1
            x -= 1
        ySize = n//2 + n//2 + n//2 + 1
        remSize = n*n-ySize
        for i in range(n):
            for j in range(n):
                if (i, j) not in visit:
                    remCount[A[i][j]] += 1
        res = inf
        for i in range(3):
            for j in range(3):
                if i == j: continue
                res = min(res, (ySize - yCount[i]) + (remSize - remCount[j]))
        return res