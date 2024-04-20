class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res, visit = [], set()
        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j] == 1 and (i, j) not in visit:
                    ans, Q = [i, j, i, j], [(i, j)]
                    while Q:
                        x, y = Q.pop(0)
                        ans[-1], ans[-2] = max(ans[-1], y), max(ans[-2], x)
                        for xx, yy in [(x+1, y), (x, y+1)]:
                            if len(land) > xx and yy < len(land[0]) and land[xx][yy] and (xx, yy) not in visit:
                                visit.add((xx, yy))
                                Q.append((xx, yy))
                    res.append(ans)
        return res