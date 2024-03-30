class Solution:
    def minimumSubarrayLength(self, A: List[int], k: int) -> int:
        res = inf
        for i in range(len(A)):
            ans = A[i]
            if A[i] >= k:
                res = 1
            for j in range(i+1, len(A)):
                ans |= A[j]
                if ans >= k:
                    res = min(res, j-i+1)
        return res if res != inf else -1