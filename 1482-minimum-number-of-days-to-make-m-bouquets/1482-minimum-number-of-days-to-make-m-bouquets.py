class Solution(object):
    def isValid(self, day, m, k, curr):
        taken, count = 0, 0
        for val in day:
            if curr >= val:
                taken += 1
            else:
                taken = 0
            if taken == k:
                count += 1
                taken = 0
        return count >= m

    def minDays(self, day, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(day)
        if n < m * k: return -1
        l, r = 0, max(day)
        res = r
        while r >= l:
            mid = (r + l) // 2
            if self.isValid(day, m, k, mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res