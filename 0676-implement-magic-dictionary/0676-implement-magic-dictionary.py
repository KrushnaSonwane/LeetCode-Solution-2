class Trie:
    def __init__(self):
        self.hashT = {}
        self.leaf = False

class MagicDictionary:

    def __init__(self):
        self.obj = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            a = self.obj
            for ch in word:
                if ch not in a.hashT:
                    a.hashT[ch] = Trie()
                a = a.hashT[ch]
            a.leaf = True

    def search(self, W: str) -> bool:
        @cache
        def dfs(i, a, change):
            if i == len(W):
                return change and a.leaf
            res = False
            if not change:
                for ch in a.hashT:
                    if ch == W[i]: continue
                    res = res or dfs(i+1, a.hashT[ch], True)
            if W[i] in a.hashT:
                res = res or dfs(i+1, a.hashT[W[i]], change)
            return res
        return dfs(0, self.obj, False)



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)