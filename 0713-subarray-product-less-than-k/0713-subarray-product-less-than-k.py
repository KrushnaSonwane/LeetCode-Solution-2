class Solution:
    def numSubarrayProductLessThanK(self, A: List[int], k: int) -> int:
        res, count, sum_, j = 0, 0, 1, 0
        for i, num in enumerate(A):
            count, sum_ = count + 1, sum_ * num
            while i >= j and sum_ >= k:
                sum_ //= A[j]
                j, count = j + 1, count - 1
            res += count
        return res