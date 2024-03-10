class Solution:
    def maximumHappinessSum(self, A: List[int], k: int) -> int:
        count, res = 0, 0
        A.sort(reverse = True)
        for i in range(k):
            res += max(0, A[i]-count)
            count += 1
        return res