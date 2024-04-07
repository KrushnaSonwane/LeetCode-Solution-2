class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        res = [ch for ch in s]
        for i, ch in enumerate(res):
            for c in chars:
                if c == ch: break
                min_ = min(abs((ord(ch))-(ord(c)+26)), abs(ord(ch)-ord(c)))
                if k >= min_:
                    k-= min_
                    res[i] = c
                    break
        return ''.join(res)
                
        