class Solution:
    def minEnd(self, n: int, x: int) -> int:

        def getBinary(num):
            if num == 0: return []
            return getBinary(num//2) + [num%2]

        if n == 1: return x

        s, ss = [0]*30 + getBinary(x), getBinary(n-1)
        i = -1
        
        while ss:
            while s[i] == 1:
                i -= 1
            s[i] = ss.pop()
            i -= 1

        return sum((2**(i-1) * s[-i]) for i in range(1, len(s)+1))