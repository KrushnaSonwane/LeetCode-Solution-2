class Solution:
    def maxScore(self, A: List[List[int]]) -> int:
        res, left = -inf, [inf for i in range(len(A))]
        for j in range(0, len(A[0])):
            min_ = inf
            for i in range(len(A)):
                min_ = min(min_, left[i])
                res = max(res, A[i][j] - min_)
                min_ = min(min_, A[i][j])
                left[i] = min(min_, left[i])
        return res