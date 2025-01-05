class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0 for _ in s]
        for l, r, dire in shifts:
            if dire:
                pre[l] += 1
                if r + 1 < len(s):
                    pre[r+1] -= 1
            else:
                pre[l] += -1
                if r + 1 < len(s):
                    pre[r+1] += 1
        last = 0
        for i in range(len(pre)):
            pre[i] += last
            last = pre[i]
            if pre[i] >= 0:
                pre[i] %= 26
            else:
                pre[i] = -(abs(pre[i]) % 26)
        allCh = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for ii, ch in enumerate(s):
            i = allCh.index(ch)
            if pre[ii] >= 0:
                res.append(allCh[(i+pre[ii])%26])
            else:
                res.append(allCh[i+pre[ii]])
        return ''.join(res)