class Solution:
    def numberOfArrays(self, A: List[int], lower: int, upper: int) -> int:
        last, max_, min_ = 0, 0, 0
        for i in range(1, len(A)+1):
            last = last+A[i-1]
            min_, max_ = min(min_, last), max(max_, last)
        diff = max_ - min_
        return max(0, ((upper-lower) - diff)+1)