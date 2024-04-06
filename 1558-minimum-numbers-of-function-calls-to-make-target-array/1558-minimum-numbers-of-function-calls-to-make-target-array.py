class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(num):
            if num <= 1:
                return num, 0
            if num % 2:
                a, b = dfs(num-1)
                return a+1, b
            a, b = dfs(num//2)
            return a, b+1
        res, max_ = 0, 0
        for num in nums:
            a, b = dfs(num)
            res += a
            max_ = max(max_, b)
        return res + max_