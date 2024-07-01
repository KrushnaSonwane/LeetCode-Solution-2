class Solution:
    def threeConsecutiveOdds(self, A: List[int]) -> bool:
        for i in range(2, len(A)):
            if A[i] % 2 == A[i-1]%2 == A[i-2] % 2 == 1: return 1
        return 0