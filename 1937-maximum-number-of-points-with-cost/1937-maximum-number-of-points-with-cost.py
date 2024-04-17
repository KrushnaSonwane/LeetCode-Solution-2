class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        res, prev = 0, A[0].copy()
        for i in range(1, len(A)):
            left, last = [], 0
            for j in range(len(A[i])):
                left.append(max(last, prev[j]))
                last = max(last-1, prev[j]-1)
            right, last = [], 0
            for j in range(len(A[i])-1, -1, -1):
                right.append(max(last, prev[j]))
                last = max(last-1, prev[j]-1)
            right = right[::-1]
            for j in range(len(A[i])):
                prev[j] = max(left[j], right[j]) + A[i][j]
        return max(prev)