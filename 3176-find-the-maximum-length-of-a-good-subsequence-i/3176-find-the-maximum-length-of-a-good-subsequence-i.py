class Solution:
    def maximumLength(self, A: List[int], k: int) -> int:
        @cache
        def dfs(i, count):
            if i == len(A): return 0
            res = 0
            for j in range(i+1, len(A)):
                if A[i] != A[j]:
                    if count != k:
                        res = max(res, dfs(j, count+1)+1)
                    else:
                        pass
                else:
                    res = max(res, dfs(j, count) + 1)
        
            return res
        ans = 0
        for i in range(len(A)):
            ans = max(ans, dfs(i, 0) + 1)
        return ans