class Solution:
    def openLock(self, visit: List[str], target: str) -> int:
        visit = set(visit)
        if '0000' in visit: return -1
        Q, A = [(0, '0000')], ['0','1','2','3','4','5','6','7','8','9']
        while Q:
            res, s = heappop(Q)
            if s == target: return res
            for i in range(4):
                for j in [(int(s[i])+1) % 10, int(s[i])-1]:
                    t = s[:i] + A[j] + s[i+1:]
                    if t not in visit: 
                        visit.add(t)
                        heappush(Q, (res+1, t))
        return -1