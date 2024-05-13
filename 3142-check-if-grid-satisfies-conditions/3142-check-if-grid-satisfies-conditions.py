class Solution:
    def satisfiesConditions(self, A: List[List[int]]) -> bool:
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i + 1 < len(A) and A[i][j] != A[i+1][j]: return False
                if j + 1 < len(A[0]) and A[i][j] == A[i][j+1]: return False
        return True
                    