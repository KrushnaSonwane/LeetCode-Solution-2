class Solution:
    def winningPlayerCount(self, n: int, A: List[List[int]]) -> int:
        hashT = Counter()
        res = set()
        for x, y in A:
            hashT[(x, y)] += 1
            if hashT[(x, y)] == x+1:
                res.add(x)
        return len(res)