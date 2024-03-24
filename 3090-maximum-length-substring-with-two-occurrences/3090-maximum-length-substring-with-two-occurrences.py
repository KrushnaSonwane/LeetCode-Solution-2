class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                count = Counter(s[i:j+1])
                for ch in count:
                    if count[ch] > 2: break
                else:
                    res = max(res, j-i+1)
        return res