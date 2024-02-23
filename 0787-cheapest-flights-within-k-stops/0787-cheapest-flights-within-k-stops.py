class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        adj = defaultdict(list)
        for u, v, d in flights:
            adj[u].append([v, d])
        queue = [[0, -1, src]]
        heapq.heapify(queue)
        while queue:
            cost, rem, node = heapq.heappop(queue)
            if node == dst: return cost
            if rem < k:
                if dist[node] > rem:
                    dist[node] = rem
                    for child, currCost in adj[node]:
                        heapq.heappush(queue, [cost + currCost, rem + 1, child])
        return -1