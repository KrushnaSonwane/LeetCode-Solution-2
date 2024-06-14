class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res, last = 0, A[0]
        for num in A[1:]:
            if last == num:
                last += 1
                res += 1
            elif last > num:
                last += 1
                res += abs(last - num)
            else:
                last = num
        return res