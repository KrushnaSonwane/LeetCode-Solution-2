class Solution:
    def lastRemaining(self, n: int) -> int:
        l, r = 1, n
        left, size = True, 1
        while r > l:
            num = (r - l) // size + 1
            if left:
                l = l + size
                if num % 2:
                    r = r - size
            else:
                r = r - size
                if num % 2:
                    l = l + size
            left = not left
            size *= 2
        return l