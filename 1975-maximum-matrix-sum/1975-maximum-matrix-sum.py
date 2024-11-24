class Solution:
    def maxMatrixSum(self, A: List[List[int]]) -> int:
        sum_, count, min_ = 0, 0, inf
        for a in A:
            for num in a:
                if num < 0: count += 1
                sum_ += abs(num)
                min_ = min(min_, abs(num))
        print(count, sum_)
        return sum_ if count%2 == 0 else sum_ - min_*2