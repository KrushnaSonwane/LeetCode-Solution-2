class Solution:
    def minOperations(self, k: int) -> int:
        
        def check(mid, sum_, max_):
            if sum_ >= k: return True
            while mid:
                if max_ * mid + sum_ >= k:
                    return True
                max_ += 1
                sum_ += 1
                mid -= 1
            return False
        
        l, r = 0, k
        res = inf
        while r >= l:
            mid = (r + l) // 2
            if check(mid, 1, 1):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            