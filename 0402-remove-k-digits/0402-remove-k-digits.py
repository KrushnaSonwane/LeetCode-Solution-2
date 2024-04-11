class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        res, Q = [], []
        max_ = 0
        for i in range(len(nums)):
            heappush(Q, [nums[i], i])
            if i >= k:
                num, j = heappop(Q)
                res.append(num)
                max_ = j
                while Q and Q[0][1] <= max_:
                    heappop(Q)
        while res and res[0] == '0':
            res.pop(0)
        if not res: return '0'
        return ''.join(res)