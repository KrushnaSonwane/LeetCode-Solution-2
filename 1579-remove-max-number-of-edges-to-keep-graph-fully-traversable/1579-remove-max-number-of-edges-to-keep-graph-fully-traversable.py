class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
    
    def find(self, node):
        if node == self.parent[node]: return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        up, vp = self.find(u), self.find(v)
        if up == vp: return 0
        if self.rank[up] > self.rank[vp]:
            self.parent[vp] = up
        elif self.rank[vp] > self.rank[up]:
            self.parent[up] = vp
        else:
            self.parent[up] = self.parent[vp]
            self.rank[vp] += 1
        return 1

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        a, b, res = 0, 0, 0
        obj = UnionFind(n)
        obj2 = UnionFind(n)
        for ty, u, v in edges:
            if ty == 3:
                obj2.union(u, v)
                if obj.union(u, v):
                    a, b = a + 1, b + 1
                else:
                    res += 1
        for ty, u, v in edges:
            if ty == 2:
                if obj.union(u, v):
                    a += 1
                else:
                    res += 1
        for ty, u, v in edges:
            if ty == 1:
                if obj2.union(u, v):
                    b += 1
                else:
                    res += 1
                print(b)
        print(a, b, res)
        return -1 if a != n - 1 or b != n - 1 else res