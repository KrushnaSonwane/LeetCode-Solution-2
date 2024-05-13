class Solution:
    def satisfiesConditions(self, A: List[List[int]]) -> bool:
        """Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists)."""
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i + 1 < len(A) and A[i][j] != A[i+1][j]: return False
                if j + 1 < len(A[0]) and A[i][j] == A[i][j+1]: return False
        return True
                    