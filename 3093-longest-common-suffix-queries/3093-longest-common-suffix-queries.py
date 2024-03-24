class Trie:
    def __init__(self):
        self.hashT = {}
        self.min_ = 0


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        obj = Trie()
        mn, size = 0, inf
        for i, ch in enumerate(wordsContainer):
            if len(ch) < size:
                size, mn = len(ch), i
        obj.min_ = mn
        wordsContainer = sorted([[len(ch), i, ch] for i, ch in enumerate(wordsContainer)])
        for _, i, w in wordsContainer:
            a = obj
            for ch in w[::-1]:
                if ch not in a.hashT:
                    a.hashT[ch] = Trie()
                    a.hashT[ch].min_ = i
                a = a.hashT[ch]
        res = [wordsContainer[0][1] for _ in range(len(wordsQuery))]
        print(res)
        for i, w in enumerate(wordsQuery):
            a = obj
            for ch in w[::-1]:
                if ch not in a.hashT:
                    break
                a = a.hashT[ch]
            res[i] = a.min_
        return res