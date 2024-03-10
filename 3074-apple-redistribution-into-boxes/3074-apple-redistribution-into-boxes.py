class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sum_ = sum(apple)
        res = 0
        for num in sorted(capacity)[::-1]:
            if sum_ <= 0: break
            sum_ -= num
            res += 1
        return res