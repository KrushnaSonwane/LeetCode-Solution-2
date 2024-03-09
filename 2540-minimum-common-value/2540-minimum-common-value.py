class Solution:
    def getCommon(self, A: List[int], B: List[int]) -> int:
        i = 0
        for num in A:
            while i < len(B) and B[i] < num:
                i += 1
            if i < len(B) and B[i] == num: return num
        return -1