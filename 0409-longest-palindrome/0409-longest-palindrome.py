class Solution:
    def longestPalindrome(self, s: str) -> int:
        A = Counter(s)
        odd, res = 0, 0
        for val in A.values():
            res += val - (val % 2)
            odd = max(odd, val % 2)
        return res + odd