class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        queue = []
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visit:
                    visit.add((i, j))
                    queue.append([i, j])
                    while queue:
                        row, col = queue.pop(0)
                        if row >= 1 and grid[row - 1][col] == '1' and (row - 1, col) not in visit:
                            visit.add((row - 1, col))
                            queue.append([row - 1, col])
                        if col >= 1 and grid[row][col - 1] == '1' and (row, col - 1) not in visit:
                            visit.add((row, col - 1))
                            queue.append([row, col - 1])
                        if m > row + 1 and grid[row + 1][col] == '1' and (row + 1, col) not in visit:
                            visit.add((row + 1, col))
                            queue.append([row + 1, col])
                        if n > col + 1 and grid[row][col + 1] == '1' and (row, col + 1) not in visit:
                            visit.add((row, col + 1))
                            queue.append([row, col + 1])
                    res += 1
        return res