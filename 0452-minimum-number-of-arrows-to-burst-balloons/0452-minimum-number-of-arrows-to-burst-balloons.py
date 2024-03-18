class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        res, min_ = 0, -inf
        for l, r in sorted(A):
            if l > min_:
                res, min_ = res + 1, r
            else:
                min_ = min(min_, r)
        return res
