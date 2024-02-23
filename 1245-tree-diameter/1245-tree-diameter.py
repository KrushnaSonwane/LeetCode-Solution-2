class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res = [0]
        def dfs(i, last):
            A = [0, 0]
            for child in adj[i]:
                if child == last: continue
                A.append(dfs(child, i))
            A.sort()
            res[0] = max(res[0], A[-1]+A[-2])
            return A[-1]+1
        dfs(0, -1)
        return res[0]