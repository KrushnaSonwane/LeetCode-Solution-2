class FrontMiddleBackQueue:

    def __init__(self):
        self.Q = []

    def pushFront(self, val: int) -> None:
        self.Q.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        if not self.Q:
            self.Q.append(val)
        else:
            self.Q.insert((len(self.Q)) // 2, val)

    def pushBack(self, val: int) -> None:
        self.Q.append(val)        

    def popFront(self) -> int:
        if not self.Q: return -1
        return self.Q.pop(0)

    def popMiddle(self) -> int:
        if not self.Q: return -1
        return self.Q.pop(((len(self.Q) - 1) // 2))

    def popBack(self) -> int:
        if not self.Q: return -1
        return self.Q.pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()