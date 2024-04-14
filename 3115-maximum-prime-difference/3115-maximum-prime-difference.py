class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        A = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        res, last = 0, -1
        for i, num in enumerate(nums):
            if num in A:
                if last == -1:
                    last = i
                res = max(res, i - last)
        return res