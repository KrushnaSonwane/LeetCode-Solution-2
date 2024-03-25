class Solution:
    def findDuplicates(self, A: List[int]) -> List[int]:
        A.sort()
        return [A[i] for i in range(1, len(A)) if A[i] == A[i-1]]