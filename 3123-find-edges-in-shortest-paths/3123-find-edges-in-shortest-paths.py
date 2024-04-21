class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for i, (a, b, c) in enumerate(edges):
            adj[a].append([b, c, i])
            adj[b].append([a, c, i])
        res = [False for _ in edges]
        Q, dist = [(0, 0)], {}
        while Q:
            cost, node = heappop(Q)
            if node in dist and dist[node] < cost: continue
            dist[node] = cost
            # if node == n-1: break
            for child, cc, _ in adj[node]:
                if child in dist and dist[child] < cc+cost: continue
                heappush(Q, [cost+cc, child])
        @cache
        def dfs(node, cost, last):
            if node== n-1 and node in dist and dist[node] == cost: return True
            if node in dist and dist[node] < cost: return False
            ans = False
            for child, cc, i in adj[node]:
                if child == last: continue
                res[i] = dfs(child, cost+cc, node) or res[i]
                # if i == 0:
                    # print(res[i])
                ans = ans or res[i]
            return ans
        dfs(0, 0, -1)
        return res