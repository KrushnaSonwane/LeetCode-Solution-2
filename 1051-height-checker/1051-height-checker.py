class Solution:
    def heightChecker(self, A: List[int]) -> int:
        return sum(a != aa for a, aa in zip(A, sorted(A)))