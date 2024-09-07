class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            a, b = 0, 0
            for j in range(i, len(s)):
                if s[j] == '1':
                    a += 1
                else:
                    b += 1
                res += int(a <= k or b <= k)
        return res