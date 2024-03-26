class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res, sum_, count = 0, 0, 0
        for num in nums:
            if num > right:
                count, sum_ = 0, 0
            else:
                count += 1
                if left <= num <= right: sum_ = count
            res += sum_
        return res