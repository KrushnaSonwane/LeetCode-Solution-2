class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        res = []
        def dfs(i, A):
            if i == len(words):
                res.append(A.copy())
                return
            dfs(i+1, A)
            A.append(i)
            B = [num for num in A]
            dfs(i+1, B.copy())
            A.pop()
        dfs(0, [])
        ans, hashT = 0, Counter(letters)
        for li in res:
            A = Counter()
            sum_ = 0
            for i in li:
                for ch in words[i]:
                    A[ch] += 1
            for ch in A:
                if hashT[ch] >= A[ch]:
                    sum_ += score[ord(ch)-97] * A[ch]
                else:
                    break
            else:
                ans = max(ans, sum_)
        return ans