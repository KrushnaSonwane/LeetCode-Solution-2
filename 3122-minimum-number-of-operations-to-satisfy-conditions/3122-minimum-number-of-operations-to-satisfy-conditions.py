class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = {}
        for j in range(n):
            count[j] = Counter()
        for i in range(m):
            for j in range(n):
                count[j][grid[i][j]] += 1
        res = 0
        @cache
        def dfs(i, last):
            if i == n: return 0
            res = m + dfs(i+1, 11)
            for num in count[i]:
                if num != last:
                    res = min(res, dfs(i+1, num) + (m-count[i][num]))
                else:
                    for numm in count[i]:
                        if numm == last: continue
                        res = min(res, dfs(i+1, numm) + (m-count[i][numm]))
            return res
            return res
        res = inf
        for num in count[0]:
            res = min(res, dfs(1, num) + (m-count[0][num]))
        return res
        