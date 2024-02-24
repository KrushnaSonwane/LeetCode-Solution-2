class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
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
        self.find(u)
        self.find(v)
        return self.parent[u] == self.parent[v]

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