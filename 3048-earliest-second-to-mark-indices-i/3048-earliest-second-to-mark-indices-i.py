class Solution:
    def earliestSecondToMarkIndices(self, A: List[int], C: List[int]) -> int:

        def check(key):
            visit, size = set(), 0
            for i in range(key-1, -1, -1):
                if C[i] not in visit:
                    visit.add(C[i])
                    size += A[C[i]-1]
                else:
                    size -= 1
                size = max(size, 0)
            return size == 0 and len(visit) == len(A)

        l, r = 1, len(C)
        res = inf
        while r >= l:
            mid = (r + l) // 2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1 

        return -1 if res == inf else res