class Solution:
    def maxScore(self, A: List[List[int]]) -> int:
        res = []
        for i in range(len(A)):
            for j in range(len(A[i])):
                res.append([A[i][j], i])
        res.sort(reverse = True)
        @cache
        def dfs(i, mask):
            if i == len(res):
                return 0
            ans = dfs(i+1, mask)
            A = [ch for ch in mask]
            if A[res[i][1]] == '0':
                A[res[i][1]] = '1'
                while i+1 < len(res) and res[i][0] == res[i+1][0]:
                    i += 1
                ans = max(ans, res[i][0] + dfs(i+1, ''.join(A.copy())))
            return ans
        return dfs(0, '0'*len(A))