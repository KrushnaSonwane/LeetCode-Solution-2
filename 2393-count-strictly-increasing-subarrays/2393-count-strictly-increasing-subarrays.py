class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        size, res = 0, 0
        last = 0
        for num in nums:
            if num > last:
                size += 1
            else:
                size = 1
            res += size
            last = num
        return res