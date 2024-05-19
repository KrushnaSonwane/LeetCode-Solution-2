class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        hashT = Counter()
        A = Counter()
        for num in nums:
            count = 0
            curr = num
            while curr:
                hashT[(count, curr % 10)] += 1
                curr //= 10
                A[count] += 1
                count += 1
        res = 0
        for num in nums:
            count = 0
            curr = num
            while curr:
                hashT[(count, curr % 10)] -= 1
                curr //= 10
                A[count] -= 1
                count += 1
            curr, count = num, 0
            while curr:
                res += A[count] - hashT[(count, curr % 10)]
                count += 1
                curr //= 10
        return res