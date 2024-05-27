class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hashT = Counter()
        res = []
        count = 0
        A = {}
        for a, b in queries:
            if a not in A:
                A[a] = b
                hashT[b] += 1
                if hashT[b] == 1:
                    count += 1
            else:
                hashT[A[a]] -= 1
                if hashT[A[a]] == 0:
                    count -= 1
                A[a] = b
                hashT[b] += 1
                if hashT[b] == 1:
                    count += 1
            res.append(count)
        return res