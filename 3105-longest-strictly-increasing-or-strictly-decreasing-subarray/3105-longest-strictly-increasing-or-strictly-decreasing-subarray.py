class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        count, last = 0, -inf
        for i in range(len(nums)):
            if nums[i] > last:
                count += 1
            else:
                count = 1
            last = nums[i]
            res = max(res, count)
        count, last = 0, inf
        for i in range(len(nums)):
            if nums[i] < last:
                count += 1
            else:
                count = 1
            last = nums[i]
            res = max(res, count)
        return res