class Solution:
    def maximumHappinessSum(self, A: List[int], k: int) -> int:
        res = 0
        A.sort(reverse = True)
        for i in range(k):
            res += max(0, A[i]-i)
        return res