class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, sqrt(c)
        high = int(high) + 1
        for num in range(high + 1):
            l, h = num, high
            while h >= l:
                mid = (l + h) // 2
                power = (num ** 2) + (mid ** 2)
                if power > c:
                    h = mid - 1
                elif power < c:
                    l = mid + 1
                else: return True
        return False