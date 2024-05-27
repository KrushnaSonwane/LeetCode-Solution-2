class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        A = Counter(nums)
        res = -1
        for num in A:
            if A[num] == 2:
                if res == -1:
                    res = num
                else:
                    res = res ^ num
        return 0 if res == -1 else res