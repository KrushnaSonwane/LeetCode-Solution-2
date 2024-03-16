class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_, A = 0, {0:-1}
        res = 0
        for i, num in enumerate(nums):
            sum_ += 1 if num else -1
            key = sum_-0
            if key in A:
                res = max(res, (i-A[key]))
            if sum_ not in A:
                A[sum_] = i
        return res