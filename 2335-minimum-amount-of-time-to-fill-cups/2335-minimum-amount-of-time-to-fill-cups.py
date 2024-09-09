class Solution:
    def fillCups(self, A: List[int]) -> int:
        Q = [-num for num in A if num != 0]
        res = 0
        while len(Q) > 1:
            a, b = heappop(Q), heappop(Q)
            res += 1
            if a + 1 != 0:
                heappush(Q, a+1)
            if b + 1 != 0:
                heappush(Q, b+1)
        if Q:
            return res - heappop(Q)
        return res