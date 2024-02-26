class Solution:
    def matrixMedian(self, A: List[List[int]]) -> int:
        Q, count = [], (len(A)*len(A[0])) // 2
        for i in range(len(A)):
            heappush(Q, [A[i][0], i, 0])
        while count != 0:
            _, i, j = heappop(Q)
            if j + 1 < len(A[0]):
                heappush(Q, [A[i][j+1], i, j+1])
            count -= 1
        return heappop(Q)[0]