class Solution:
    def islandPerimeter(self, A: List[List[int]]) -> int:
        res = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j]:
                    for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0 <= x < len(A) and 0 <= y < len(A[i]) and A[x][y]: 
                            continue
                        res += 1
        return res
