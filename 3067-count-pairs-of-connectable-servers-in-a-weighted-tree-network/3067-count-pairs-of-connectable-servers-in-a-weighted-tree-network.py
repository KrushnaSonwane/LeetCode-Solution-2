class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], S: int) -> List[int]:
        
        def dfs(node, sum_, count, last):
            if sum_ % S == 0:
                self.count += 1
            for child, c in adj[node]:
                if child == last: continue
                dfs(child, sum_+c, count, node)
                
                
        
        adj = defaultdict(list)
        for a, b, c in edges:
            adj[a].append([b, c])
            adj[b].append([a, c])
        res = []
        A = []
        for i in range(len(edges)+1):
            A = []
            if len(adj[i]) == 1:
                res.append(0)
            else:
                for child, c in adj[i]:
                    self.count = 0
                    dfs(child, c, 0, i)
                    A.append(self.count)
                ans, sum_ = 0, 0
                for num in A:
                    if num == 0: continue
                    ans += num * sum_
                    sum_ += num
                res.append(ans)
            # print(A)
        return res