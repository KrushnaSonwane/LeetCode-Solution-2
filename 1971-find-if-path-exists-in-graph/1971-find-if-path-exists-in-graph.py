class UF:
    def __init__(self, n):
        self.rank = [0 for _ in range(n)]
        self.p = [i for i in range(n)]
    
    def find(self, node):
        if node == self.p[node]: return node
        self.p[node] = self.find(self.p[node])
        return self.p[node]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v: return
        if self.rank[u] > self.rank[v]:
            self.p[v] = u
        else:
            self.p[u] = v
            self.rank[v] += 1

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UF(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.find(source) == uf.find(destination)