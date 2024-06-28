class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hashT = Counter()
        for a, b in roads:
            hashT[a] += 1
            hashT[b] += 1
        A = sorted([[hashT[a], a] for a in hashT])[::-1]
        res = 0
        for a, b in A:
            res += (a * n)
            n -= 1
        return res