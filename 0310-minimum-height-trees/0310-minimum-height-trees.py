class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        D, A = Counter(), defaultdict(list)
        for a, b in edges:
            A[a].append(b)
            A[b].append(a)
            D[a] += 1; D[b] += 1
        Q = []
        for i in range(n):
            if D[i] == 1:
                Q.append(i)
                D[i] -= 1
        res = []
        while Q:
            res = Q.copy()
            for _ in range(len(Q)):
                node = Q.pop(0)
                for child in A[node]:
                    D[child] -= 1
                    if D[child] == 1: Q.append(child)
        return res