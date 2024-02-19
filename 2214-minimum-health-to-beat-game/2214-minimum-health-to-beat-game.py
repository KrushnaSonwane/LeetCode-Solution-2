class Solution:
    def minimumHealth(self, A: List[int], armor: int) -> int:
        max_, sum_ = max(A), sum(A)
        if max_ >= armor: return (sum_-armor)+1
        return (sum_ - max_) + 1