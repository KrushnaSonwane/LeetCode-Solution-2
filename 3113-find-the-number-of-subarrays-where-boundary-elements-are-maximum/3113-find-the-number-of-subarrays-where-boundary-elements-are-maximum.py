class SEG:
    def __init__(self, A):
        self.hashT = {}
        self.A = A
    
    def getMax(self, l, r):
        if l == r:
            self.hashT[(l, r)] = self.A[l]
            return self.A[l]
        mid = (l+r) // 2
        ans = [self.getMax(l, mid), self.getMax(mid+1, r)]
        self.hashT[(l, r)] = ans
        return max(ans)
        
    def getRange(self, l, r, ll, rr):
        if l == r: return self.hashT[(l, r)]
        if ll <= l <= r <= rr: 
            return max(self.hashT[(l, r)])
        mid = (l+r) // 2
        if mid < ll:
            ans = self.getRange(mid+1, r, ll, rr)
        elif mid >= rr:
            ans =self.getRange(l, mid, ll, rr)
        else:
            ans = max(self.getRange(l, mid, ll, rr), self.getRange(mid+1, r, ll, rr))
        return ans

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        obj = SEG(nums)
        obj.getMax(0, len(nums)-1)
        hashT = defaultdict(list)
        for i, num in enumerate(nums):
            hashT[num].append(i)
        res = 0
        for num in hashT:
            last = -1
            count = 0
            for i in hashT[num]:
                if last == -1:
                    last = i
                max_ = obj.getRange(0, len(nums)-1, last, i)
                if max_ == num:
                    last = i
                    count += 1
                else:
                    count = 1
                last = i
                res += count
        return res
                