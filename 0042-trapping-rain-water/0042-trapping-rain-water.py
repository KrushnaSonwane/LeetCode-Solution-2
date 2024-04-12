class Solution:
    def trap(self, A: List[int]) -> int:
        max_, left = 0, []
        for num in A:
            max_ = max(max_, num)
            left.append(max_)
        max_, right = 0, []
        for num in A[::-1]:
            max_ = max(max_, num)
            right.append(max_)
        return sum(min(a, c) - b for a, b, c in zip(left, A, right[::-1]))