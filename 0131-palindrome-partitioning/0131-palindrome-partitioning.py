class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pal = [[False for _ in s] for _ in s]
        def check(i, j):
            if i >= j: return True
            if s[i] != s[j]: return False
            return check(i+1, j-1)
        for i in range(len(s)):
            for j in range(i, len(s)):
                pal[i][j] = check(i, j)
        res = []
        def dfs(i, j, A):
            if i == len(s): return
            if j == len(s):
                if pal[i][j-1]:
                    A.append(s[i:j])
                    res.append(A.copy())
                    A.pop()
                return 
            dfs(i, j+1, A)
            if pal[i][j]:
                A.append(s[i:j+1])
                B = [ch for ch in A]
                dfs(j+1, j+1, B.copy())
                A.pop()
        dfs(0, 0, [])
        return res