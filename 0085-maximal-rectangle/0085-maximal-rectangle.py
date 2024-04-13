class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        res = 0
        arr = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0': arr[j] = 0
                else: arr[j] += 1
            nSmall, pSmall = [], []
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if not stack: nSmall.append(n)
                else: nSmall.append(stack[-1])
                stack.append(i)
            stack = []
            nSmall = nSmall[::-1]
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if not stack: pSmall.append(-1)
                else: pSmall.append(stack[-1])
                stack.append(i)
            for i in range(n):
                if pSmall[i] == -1:
                    res = max(res, arr[i] * nSmall[i])
                else:
                    res = max(res, arr[i] * (nSmall[i] - pSmall[i] - 1))
        return res