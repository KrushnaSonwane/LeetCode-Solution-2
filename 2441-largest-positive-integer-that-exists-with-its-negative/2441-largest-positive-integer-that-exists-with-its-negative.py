class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hashT = {}
        ans = 0
        for n in nums:
            if 0 > n:
                if abs(n) in hashT and ans < abs(n):
                    ans = abs(n)
                hashT[n] = 0
            else:
                if -(n) in hashT and ans < n:
                    ans = n
                hashT[n] = 0
        if ans == 0: return -1
        return ans