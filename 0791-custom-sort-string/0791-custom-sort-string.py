class Solution:
    def customSortString(self, order: str, s: str) -> str:
        A = Counter(s)
        res = []
        for ch in order:
            res.append(A[ch]*ch)
            A[ch] = 0
        for ch in sorted(A.keys()):
            res.append(ch*A[ch])
        return ''.join(res)