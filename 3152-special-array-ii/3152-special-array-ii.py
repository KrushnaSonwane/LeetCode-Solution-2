class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        A = []
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                A.append(i)
        res = []
        for a, b in queries:
            if a == b:
                res.append(True)
            else:
                l, r = 0, len(A)-1
                while r >= l:
                    mid = (r+l) // 2
                    if A[mid] > b:
                        r = mid-1
                    else:
                        if A[mid] > a:
                            res.append(False)
                            break
                        l = mid + 1
                else:
                    res.append(True)
        return res