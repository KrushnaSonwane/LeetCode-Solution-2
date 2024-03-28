class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        A, j, res = Counter(), 0, 0
        for i, num in enumerate(nums):
            A[num] += 1
            while A[num] > k:
                A[nums[j]] -= 1
                j += 1
            res = max(res, i-j+1)
        return res