class Solution:
    def minimumTime(self, n: int, A: List[List[int]], B: List[int]) -> List[int]:
        A.sort(key = lambda x: (x[2]))
        uq = defaultdict(set)
        hashT = defaultdict(list)
        for a, b, c in A:
            if a == b: continue
            if b not in uq[a]:
                hashT[a].append([b, c])
                uq[a].add(b)
            if a not in uq[b]:
                uq[b].add(a)
                hashT[b].append([a, c])
        dist = {i: inf for i in range(n)}
        # dist[0] = 0
        Q = [(0, 0)]
        while Q:
            cost, node = heappop(Q)
            if dist[node] <= cost or B[node] <= cost: continue
            dist[0]=0
            dist[node] = cost
            for child, c in hashT[node]:
                if cost+c >= dist[child]: continue
                heappush(Q, [c+cost, child])

        res = []
        for i in range(len(B)):
            if dist[i] == inf:
                res.append(-1)
            else:
                res.append(dist[i])
        return res