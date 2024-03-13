class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            lSum, rSum = 0, 0
            for a in range(1, i+1):
                lSum += a
            for a in range(i, n+1):
                rSum += a
            if lSum == rSum: return i
        return -1