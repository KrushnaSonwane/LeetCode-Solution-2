class Solution:
    def minOperationsToMakeMedianK(self, A: List[int], k: int) -> int:
        A.sort()
        idx, res = len(A) // 2, 0
        for i in range(idx-1, -1, -1):
            if A[i] <= k: continue
            res += abs(k-A[i])
        for i in range(idx+1, len(A)):
            if A[i] >= k: continue
            res += abs(k-A[i])
        return res + abs(A[idx]-k)