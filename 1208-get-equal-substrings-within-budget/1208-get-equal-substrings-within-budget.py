class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        A = []
        for a, b in zip(s, t):
            A.append(abs(ord(a) - ord(b)))
        res, sum_ = 0, 0
        i, j = 0, 0
        while j < len(s):
            sum_ += A[j]
            while sum_ > maxCost:
                sum_ -= A[i]
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res
