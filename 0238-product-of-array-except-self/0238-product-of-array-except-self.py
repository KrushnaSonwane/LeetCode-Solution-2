class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for _ in nums]
        sum_ = nums[0]
        for i in range(1, len(nums)):
            res[i] = sum_
            sum_ *= nums[i]
        sum_ = nums[-1]
        for i in range(len(nums)-2, 0, -1):
            res[i] *= sum_
            sum_ *= nums[i]
        res[0] = sum_
        return res