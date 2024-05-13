class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    res += abs(i - j)
        return res