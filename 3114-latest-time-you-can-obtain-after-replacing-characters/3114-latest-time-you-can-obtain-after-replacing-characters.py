class Solution:
    def findLatestTime(self, s: str) -> str:
        for HH in range(11, -1, -1):
            for MM in range(59, -1, -1):
                HH, MM = str(HH), str(MM)
                if len(HH) == 1:
                    HH = '0'+HH
                if len(MM) == 1:
                    MM = '0'+MM
                if (HH[0] == s[0] or s[0] == '?') and (HH[1] == s[1] or s[1] == '?') and (MM[0] == s[3] or s[3] == '?') and (MM[1] == s[-1] or s[-1] == '?'):
                    return HH + ':' + MM
        