class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.res = [0, '0'*12]
        def dfs(i, sum_, A, score):
            if i == len(A): 
                if score > self.res[0]:
                    self.res = [score, A]
                return
            dfs(i+1, sum_, A, score)
            if sum_ > aliceArrows[i]:
                A = list(A)
                A[i] = '1'
                dfs(i+1, sum_ - (aliceArrows[i]+1), ''.join(A), i+score)
        dfs(0, numArrows, '0'*12, 0)
        ans = []
        for i in range(12):
            ans.append((aliceArrows[i] + 1) if self.res[1][i] == '1' else 0)
        ans[0] = numArrows-sum(ans)
        return ans