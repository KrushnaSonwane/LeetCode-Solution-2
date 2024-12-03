class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        i, j = 0, 0
        while i < len(s):
            if len(spaces) > j and i == spaces[j]:
                res.append(" ")
                j += 1
            res.append(s[i])
            i += 1
        return ''.join(res)