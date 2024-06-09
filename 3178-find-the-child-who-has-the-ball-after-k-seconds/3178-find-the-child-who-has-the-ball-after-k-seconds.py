class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        i, f = 0, True
        for _ in range(k):
            if f:
                i += 1
            else:
                i -= 1
            if i == -1:
                f, i = 1, 1
            if i == n:
                f, i = 0, n-2
        return i