class Solution:
    def timeRequiredToBuy(self, A: List[int], k: int) -> int:
        A, res = [[i, time] for i, time in enumerate(A)], 0
        while True:
            res += 1
            i, a = A.pop(0)
            if a == 1 and i == k: return res
            if a - 1 >= 1:
                A.append([i, a-1])
        return 0