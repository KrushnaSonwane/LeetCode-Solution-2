class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res, sum_ = 0, 0
        i = 0
        while sum_ < n:
            while i < len(nums) and nums[i] <= sum_+1:
                sum_ += nums[i]
                i += 1
            if sum_ >= n: break
            if i < len(nums):
                if nums[i] > sum_ + 1:
                    sum_ += sum_ + 1
                res += 1
            if sum_ >= n: break
            while i == len(nums) and sum_ < n:
                sum_ += sum_ + 1
                res += 1
        return res