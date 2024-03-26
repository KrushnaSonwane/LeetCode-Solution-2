class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        A, num = set(A), 1
        while num in A:
            num += 1
        return num