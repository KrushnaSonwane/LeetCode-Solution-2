class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        sum_, n = 0, 1
        size = 1
        while sum_ < neededApples:
            sum_ += (n * (n + 1) // 2) * 8
            sum_ += n * (size * 4)
            size += 2
            n += 1
        return (size-1) * 4