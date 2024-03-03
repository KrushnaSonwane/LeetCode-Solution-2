class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        A = []
        for num in nums:
            heappush(A, num)
        res = 0
        while len(A) >= 2:
            x, y = heappop(A), heappop(A)
            if k > x:
                res += 1
            else:
                break
            heappush(A, min(x, y) * 2 + max(x, y))
        return res