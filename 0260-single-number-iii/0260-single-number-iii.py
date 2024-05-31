class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        A = Counter(nums)
        res = []
        for i in range(len(nums)):
            if A[nums[i]] == 1: res.append(nums[i])
        return res