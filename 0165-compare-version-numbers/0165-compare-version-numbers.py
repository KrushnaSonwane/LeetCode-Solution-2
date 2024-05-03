class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        p1, p2 = 0, 0
        n, m = len(v1), len(v2)
        an1, an2 = 0, 0
        while p1 < n or p2 < m:
            num1, num2 = 0, 0
            flag1, flag2 = False, False
            while p1 < n:
                if v1[p1] == '.': 
                    p1 += 1
                    break
                num1 = (num1 * 10) + int(v1[p1])
                flag1 = True
                p1 += 1
            while p2 < m:
                if v2[p2] == '.': 
                    p2 += 1
                    break
                num2 = (num2 * 10) + int(v2[p2])
                flag2 = True
                p2 += 1
            if flag1 and flag2:
                if num1 > num2: return 1
                if num2 > num1: return -1
            elif flag1:
                if num1 >= 1: return 1
            elif flag2:
                if num2 >= 1: return -1
        return 0