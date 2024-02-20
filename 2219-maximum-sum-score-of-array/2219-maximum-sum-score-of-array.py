class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        sum_, res = 0, -inf
        for i in range(len(nums)):
            sum_ += nums[i]
            res = max(res, sum_)
        sum_ = 0
        for i in range(len(nums)-1,-1,-1):
            sum_ += nums[i]
            res = max(res, sum_)
        return res