class Solution:
    def makePalindrome(self, s: str) -> bool:
        res, l, r = 0, 0, len(s)-1
        while r >= l:
            res += s[l] != s[r]
            l, r = l + 1, r - 1
        return res <= 2