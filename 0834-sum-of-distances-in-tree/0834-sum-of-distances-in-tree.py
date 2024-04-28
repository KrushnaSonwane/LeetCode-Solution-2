class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        count, sum_ = [1 for _ in range(n)], [0 for _ in range(n)]
        
        def dfs(node, parent):
            for child in adj[node]:
                if child == parent: continue
                dfs(child, node)
                count[node] += count[child]
                sum_[node] += count[child] + sum_[child]

        def dfs2(node, parent):
            for child in adj[node]:
                if child == parent: continue
                sum_[child] += (sum_[node] - (sum_[child]+count[child]) + (n-count[child]))
                dfs2(child, node)
        dfs(0, -1)
        dfs2(0, -1)
        return sum_