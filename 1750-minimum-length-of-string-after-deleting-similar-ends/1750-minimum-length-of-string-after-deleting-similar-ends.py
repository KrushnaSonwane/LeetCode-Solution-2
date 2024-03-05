class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while r > l:
            if s[l] != s[r]: break
            ch = s[l]
            while r >= l and s[l] == ch:
                l += 1
            while r >= l and s[r] == ch:
                r -= 1
        return r - l + 1