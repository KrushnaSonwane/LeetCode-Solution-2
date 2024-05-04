class Solution:
    def numRescueBoats(self, A: List[int], limit: int) -> int:
        res = 0; A.sort()
        l, r = 0, len(A)-1
        while r >= l:
            if A[l] + A[r] <= limit:
                l += 1
            r, res = r - 1, res + 1
        return res