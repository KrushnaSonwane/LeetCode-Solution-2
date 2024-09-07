class Solution:
    def resultsArray(self, A: List[int], k: int) -> List[int]:
        if k == 1: return A
        res = []
        B = deque()
        for i in range(k-1):
            if not B or B[-1] == A[i]-1:
                B.append(A[i])
            else:
                B = deque([A[i]])
        for i in range(k-1, len(A)):  
            if B[-1] == A[i]-1:
                B.append(A[i])
            else:
                B = deque([A[i]])
            if len(B) == k:
                res.append(A[i])
                B.popleft()
            else:
                res.append(-1)
        return res