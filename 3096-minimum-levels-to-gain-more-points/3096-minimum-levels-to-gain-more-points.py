class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        lSum, rSum = 0, 0
        for i in range(len(possible)):
            rSum += 1 if possible[i] else -1
        for i in range(len(possible)-1):
            rSum += -1 if possible[i] else 1
            lSum += 1 if possible[i] else -1
            if lSum > rSum: 
                return i+1
        return -1