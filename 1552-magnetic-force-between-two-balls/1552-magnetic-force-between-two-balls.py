class Solution:
    def maxDistance(self, A: List[int], m: int) -> int:
        A.sort()
        def check(k):
            count, last = 1, A[0]
            for num in A:
                if abs(num - last) >= k:
                    last = num
                    count += 1
            return count >= m
        
        l, r = 1, 10**9
        res = 1
        while r >= l:
            mid = (r + l) // 2
            if check(mid):
                l = mid + 1
                res = mid
            else:
                r = mid - 1 
        return res