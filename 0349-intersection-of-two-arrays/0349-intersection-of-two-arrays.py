class Solution:
    def intersection(self, A: List[int], B: List[int]) -> List[int]:
        A = set(A)
        res = []
        for num in set(B):
            if num in A: res.append(num)
        return res