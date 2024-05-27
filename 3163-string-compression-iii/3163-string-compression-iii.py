class Solution:
    def compressedString(self, s: str) -> str:
        res = []
        i, j = 0, 0
        while len(s) > i:
            count = 0
            while count < 9 and j < len(s) and s[i] == s[j]:
                count += 1
                j += 1
            
            res.append(str(count)+s[i])
            i = j
        return ''.join(res)