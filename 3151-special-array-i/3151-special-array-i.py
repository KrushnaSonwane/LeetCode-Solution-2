class Solution:
    def isArraySpecial(self, A: List[int]) -> bool:
        for i in range(1, len(A)):
            if A[i-1] % 2 == A[i] % 2: return False
        return True