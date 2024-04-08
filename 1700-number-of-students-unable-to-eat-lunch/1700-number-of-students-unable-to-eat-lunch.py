class Solution:
    def countStudents(self, A: List[int], B: List[int]) -> int:
        res, change = 0, 0
        while A and B and change <= len(A):
            if A[0] == B[0]:
                A.pop(0)
                B.pop(0)
                change = 0
            else:
                change += 1
                A.append(A.pop(0))
        return len(A)