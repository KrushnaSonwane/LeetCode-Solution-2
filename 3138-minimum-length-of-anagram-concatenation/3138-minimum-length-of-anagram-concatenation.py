class Solution:
    def minAnagramLength(self, s: str) -> int:
        A = Counter(s)
        for v in A.values():
            res = v
        for ch in A:
            res = gcd(res, A[ch])
        return len(s) // res