class Solution:
    def specialArray(self, A: List[int]) -> int:
        for i in range(1, len(A)+1):
            count = 0
            for num in A:
                if num >= i: count += 1
            if count == i: return i
        return -1