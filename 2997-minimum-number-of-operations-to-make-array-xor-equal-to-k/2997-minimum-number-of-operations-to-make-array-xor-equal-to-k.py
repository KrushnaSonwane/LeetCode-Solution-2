class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(25):
            xor = 0
            for num in nums:
                xor = xor ^ ((num >> i) & 1)
            if xor != (k >> i) & 1:
                res += 1
        return res