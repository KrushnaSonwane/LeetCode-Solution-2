class Solution:
    def maximumSubarraySum(self, A: List[int], k: int) -> int:
        hashT, count, sum_ = Counter(), 0, 0
        res = 0
        for i in range(k-1):
            sum_ += A[i]
            hashT[A[i]] += 1
            if hashT[A[i]] == 1:
                count += 1
        for i in range(k-1, len(A)):
            sum_ += A[i]
            hashT[A[i]] += 1
            if hashT[A[i]] == 1:
                count += 1
            if count == k:
                res = max(res, sum_)
            sum_ -= A[i-(k-1)]
            hashT[A[i-(k-1)]] -= 1
            if hashT[A[i-(k-1)]] == 0:
                count -= 1
            # print(count, sum_)
        return res