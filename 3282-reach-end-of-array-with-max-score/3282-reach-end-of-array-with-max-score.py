class Solution:
    def findMaximumScore(self, A: List[int]) -> int:
        res, last, max_ = 0, 0, A[0]
        for i in range(1, len(A)):
            if A[i] > max_:
                res += (i - last) * max_
                max_, last = A[i], i
        return res if last == len(A) - 1 else res + ((len(A)-1)-last) * max_