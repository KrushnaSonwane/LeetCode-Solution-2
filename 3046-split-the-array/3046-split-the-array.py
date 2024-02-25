class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        A = Counter(nums)
        for num in A.values():
            if num > 2: return False
        return True