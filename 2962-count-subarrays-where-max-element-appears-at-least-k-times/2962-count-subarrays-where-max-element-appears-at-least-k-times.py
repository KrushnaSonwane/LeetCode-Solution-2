class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        res, max_ = 0, max(A)
        size = count = j = 0
        for i, a in enumerate(A):
            count += max_ == a
            while count == k and A[j] != max_:
                j, size = j+1, size+1
            if count == k:
                res += (size+1) * (len(A) - i)
                j, count = j+1, count - 1
                size = 0
        return res