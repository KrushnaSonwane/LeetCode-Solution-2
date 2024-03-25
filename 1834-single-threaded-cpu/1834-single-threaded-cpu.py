class Solution:
    def getOrder(self, A: List[List[int]]) -> List[int]:
        res, A = [], sorted([[a, b, i] for i, (a, b) in enumerate(A)])
        time, Q = 0, []
        while Q or A:
            while not Q or (A and time >= A[0][0]):
                a, b, i = A.pop(0)
                heappush(Q, [b, i])
                time = max(time, a)
            b, i = heappop(Q)
            time += b
            res.append(i)
        return res