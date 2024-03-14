class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        A = Counter()
        A[0], res, sum_ = 1, 0, 0
        for num in nums:
            sum_ += num
            res += A[sum_-goal]
            A[sum_] += 1
        return res