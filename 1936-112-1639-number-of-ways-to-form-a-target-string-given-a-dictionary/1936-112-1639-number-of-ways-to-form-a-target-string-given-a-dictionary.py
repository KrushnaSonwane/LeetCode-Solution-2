class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        hashT = defaultdict()
        for i in range(len(words[0])):
            hashT[i] = Counter()
        for i, w in enumerate(words):
            for j, ch in enumerate(w):
                hashT[j][ch] += 1
        @cache
        def dfs(i, j):
            if j == len(target): return 1
            if i == len(words[0]): return 0
            res = dfs(i+1, j)
            res += dfs(i+1, j+1) * hashT[i][target[j]]
            return res % (10**9+7)
        return dfs(0, 0)