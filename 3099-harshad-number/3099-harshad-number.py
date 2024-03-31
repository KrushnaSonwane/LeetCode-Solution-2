class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x = str(x)
        sum_ = 0
        for num in x:
            sum_ += int(num)
        return sum_ if int(x) % sum_ == 0 else -1