class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        ss = s[::-1]
        for i in range(1, len(s)):
            if s[i-1: i+1] in ss: return True
        return False