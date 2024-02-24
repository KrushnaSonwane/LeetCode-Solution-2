class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)]
    
    def find(self, node):
        if node == self.parent[node]: return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v: return
        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        elif self.rank[u] < self.rank[v]:
            self.parent[u] = v
        else:
            self.parent[v] = u
            self.rank[u] += 1
    
    def check(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def findAllPeople(self, n: int, A: List[List[int]], firstPerson: int) -> List[int]:
        A.sort(key = lambda x: (x[2]))
        obj = UnionFind(n)
        obj.union(0, firstPerson)
        i = 0
        while i < len(A):
            time = A[i][2]
            curr = []
            while i < len(A) and A[i][2] == time:
                x, y = A[i][0], A[i][1]
                obj.union(x, y)
                curr.extend([x, y])
                i += 1
            for node in curr:
                if obj.find(node) != obj.find(0):
                    obj.parent[node] = node
        return [node for node in range(n) if obj.check(0, node)]