class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):
                A, sum_ = [0 for _ in range(16)], set()
                for a in range(i-2, i+1):
                    sm = 0
                    for b in range(j-2, j+1):
                        A[grid[a][b]] = 1
                        sm += grid[a][b]
                    sum_.add(sm)
                for b in range(j-2, j+1):
                    sm = 0
                    for a in range(i-2, i+1):
                        sm += grid[a][b]
                    sum_.add(sm)
                sum_.add(grid[i][j]+grid[i-1][j-1]+grid[i-2][j-2])
                sum_.add(grid[i][j-2]+grid[i-1][j-1]+grid[i-2][j])
                res += sum(A[1:10]) == 9 and len(sum_) == 1
        return res