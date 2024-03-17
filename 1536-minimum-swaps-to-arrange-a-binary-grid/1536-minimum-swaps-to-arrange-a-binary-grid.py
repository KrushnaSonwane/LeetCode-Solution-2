class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        A = []
        for i in range(len(grid)):
            count = 0
            for j in range(len(grid)-1, -1, -1):
                if grid[i][j] == 1: break
                count += 1
            A.append(count)
        res, i = 0, 0
        for size in range(len(A)-1, 0, -1):
            if A[i] < size:
                j = i+1
                while j < len(A):
                    if A[j] >= size:
                        break
                    j += 1
                else: return -1
                while j != i:
                    A[j], A[j-1] = A[j-1], A[j]
                    j -= 1
                    res += 1
            i += 1
        return res