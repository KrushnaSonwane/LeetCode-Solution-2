class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], R: List[int]) -> int:
        A = sorted([[max(0, l-s), min(n-1, l+s)] for l, s in lights])
        stack, res, j = [], 0, 0
        for i in range(n):
            while stack and stack[0] < i:
                heappop(stack)
            while j < len(A) and A[j][0] <= i:
                heappush(stack, A[j][1])
                j += 1
            res += len(stack) >= R[i]
        return res