class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            num = str(num)
            max_ = '0'
            for n in num:
                max_ = max(max_, n)
            A = [max_ for _ in num]
            A = ''.join(A)
            res += int(A)
        return res
            
            