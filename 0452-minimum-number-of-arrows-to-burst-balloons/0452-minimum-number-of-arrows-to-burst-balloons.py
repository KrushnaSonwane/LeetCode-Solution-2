class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        res, min_ = 0, -inf
        for l, r in sorted(A):
            if l > min_:
                min_ = r
                res += 1
            else:
                min_ = min(min_, r)
        return res
