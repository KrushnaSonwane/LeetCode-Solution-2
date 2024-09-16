class Solution:
    def findMinDifference(self, time: List[str]) -> int:
        A = []
        for t in time:
            A.append(int(t[0:2])*60 + int(t[3:5]))
        A.sort()
        ans = []
        for i, num in enumerate(A):
            ans.append([num, i])
            ans.append([num+1440, i])
        res = inf
        ans.sort()
        for i in range(1, len(ans)-1):
            a, b = ans[i-1]
            aa, bb = ans[i]
            if b != bb:
                res = min(res, abs(a - aa))
            else:
                if i-2 >= 0:
                    a, b = ans[i-2]
                    res = min(res, abs(a-aa))
        # print(ans)
        return res