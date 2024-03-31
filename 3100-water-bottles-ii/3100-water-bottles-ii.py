class Solution:
    def maxBottlesDrunk(self, a: int, b: int) -> int:
        res, empty = a, a
        while empty >= b:
            res += 1
            empty -= (b-1)
            b += 1
        return res