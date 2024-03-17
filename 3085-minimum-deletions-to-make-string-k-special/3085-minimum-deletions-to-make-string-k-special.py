class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        A = Counter(word)
        A = sorted([A[ch] for ch in A])
        res, sum_ = inf, 0
        for i in range(len(A)):
            curr = 0
            for j in range(i, len(A)):
                if A[j] - A[i] > k:
                    curr += A[j] - (A[i] + k)
            res = min(res, curr + sum_)
            sum_ += A[i]
        return res