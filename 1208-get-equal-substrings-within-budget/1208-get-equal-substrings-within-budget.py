class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = sum_ = i = j = 0
        while j < len(s):
            sum_ += abs(ord(s[j])-ord(t[j]))
            while sum_ > maxCost:
                sum_ -= abs(ord(s[i])-ord(t[i]))
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res
