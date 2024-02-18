class Solution:
    def longestCommonPrefix(self, A: List[int], B: List[int]) -> int:
        
        def check(k):
            hashT = set()
            for num in A:
                num = str(num)
                if len(num) >= k:
                    hashT.add(num[:k])
            for num in B:
                num = str(num)
                if num[:k] in hashT: return True
            return False
        
        res, l, r = 0, 0, 9
        while r >= l:
            mid = (r + l) // 2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res