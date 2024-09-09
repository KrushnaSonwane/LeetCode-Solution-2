class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ''
        for ch in s:
            if ch == ch.upper():
                if ch.lower() in s:
                    res = max(res, ch)
        return res