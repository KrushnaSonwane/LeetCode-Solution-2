class MagicDictionary:

    def __init__(self):
        self.hashT = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            self.hashT[len(w)].append(w)

    def search(self, searchWord: str) -> bool:
        for word in self.hashT[len(searchWord)]:
            count = 0
            for a, b in zip(word, searchWord):
                count += a != b
            if count == 1: return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)