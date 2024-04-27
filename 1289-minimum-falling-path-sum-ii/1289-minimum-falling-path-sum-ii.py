class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        def getMin(A):
            res, min_ = [], inf
            for num in A:
                res.append(min_)
                min_ = min(min_, num)
            return res

        last = A[0]
        for i in range(1, len(A)):
            left, right = getMin(last), getMin(last[::-1])[::-1]
            dp = []
            for j in range(len(A[i])):
                dp.append(min(right[j], left[j]) + A[i][j])
            last = dp
        return min(last)