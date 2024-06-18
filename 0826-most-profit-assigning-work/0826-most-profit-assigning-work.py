class Solution:
    def maxProfitAssignment(self, D: List[int], P: List[int], W: List[int]) -> int:
        A = [[profit, diff] for profit, diff in zip(D, P)]
        A.sort(); W.sort()
        res = 0
        m, n = len(A), len(W); ptr1, ptr2 = 0, 0
        max_ = 0
        while ptr2 < n:
            while ptr1 < m and W[ptr2] >= A[ptr1][0]:
                max_ = max(max_, A[ptr1][1])
                ptr1 += 1
            res += max_
            ptr2 += 1
        return res