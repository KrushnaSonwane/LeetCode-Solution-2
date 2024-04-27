class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dfs(i, j):
            if j == len(key): return 0
            if ring[i] == key[j]:
                return 1 + dfs(i, j+1)
            res, t, steps = inf, i, 1
            while ring[t] != key[j]:
                t += 1
                t %= len(ring)
                steps += 1
            res = dfs(t, j+1) + steps
            t, steps = i, 1
            while ring[t] != key[j]:
                t -= 1
                steps += 1
                if t == -1: t = len(ring)-1
            res = min(res, dfs(t, j+1) + steps)
            return res
        return dfs(0, 0)

