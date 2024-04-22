class UF:
    def __init__(self, n):
        self.r = [0 for _ in range(n)]
        self.p = [i for i in range(n)]

    def find(self, node):
        if node != self.p[node]:
            self.p[node] = self.find(self.p[node])
        return self.p[node]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v: return
        if self.r[u] > self.r[v]:
            self.p[v] = u
        else:
            self.p[u] = v
            self.r[v] += 1

class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        uf = UF(len(A))
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j] == 1:
                    uf.union(i, j)
        for i in range(len(A)):
            uf.find(i)
        return len(set(uf.p))