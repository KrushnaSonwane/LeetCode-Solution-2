class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for num in nums:
            if k > num:
                res += 1
        return res