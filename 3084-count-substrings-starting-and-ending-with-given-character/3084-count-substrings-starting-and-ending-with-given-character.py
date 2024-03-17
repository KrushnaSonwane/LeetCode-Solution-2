class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        res = 0
        for i in range(1, count+1):
            res += i
        return res