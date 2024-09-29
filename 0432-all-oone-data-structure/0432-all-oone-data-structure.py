from sortedcontainers import SortedList
class AllOne:

    def __init__(self):
        self.A = SortedList()
        self.hashT = {}

    def inc(self, key: str) -> None:
        if key not in self.hashT:
            self.hashT[key] = 1
            self.A.add([1, key])
        else:
            self.hashT[key] += 1
            self.A.discard([self.hashT[key]-1, key])
            self.A.add([self.hashT[key], key])

    def dec(self, key: str) -> None:
        self.A.discard([self.hashT[key], key])
        self.hashT[key] -= 1
        if self.hashT[key] == 0:
            del self.hashT[key]
        else:
            self.A.add([self.hashT[key], key])
            
        

    def getMaxKey(self) -> str:
        return self.A[-1][1] if self.A else ''
        

    def getMinKey(self) -> str:
        return self.A[0][1] if self.A else ''    


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()