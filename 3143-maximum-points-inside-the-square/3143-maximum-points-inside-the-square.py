class Solution:
    def maxPointsInsideSquare(self, A: List[List[int]], s: str) -> int:
        
        def check(key):
            hashT = Counter()
            for i in range(len(A)):
                x, y = A[i]
                if abs(x) <= key and abs(y) <= key:
                    hashT[s[i]] += 1
            for ch in hashT.values():
                if ch >= 2: return False, 0
            return True, len(hashT)
        
        res = 0
        l, r = 0, 10**9+1
        while r >= l:
            mid = (r + l) // 2
            ans, size = check(mid)
            if ans:
                res = max(res, size)
                l = mid + 1
            else:
                r = mid - 1
        return res