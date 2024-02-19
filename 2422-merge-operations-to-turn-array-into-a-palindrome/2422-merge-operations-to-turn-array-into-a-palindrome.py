class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        res, l, r = 0, 0, 0
        i, j = 0, len(A)-1
        while j >= i:
            if l == r:
                r += A[j]
                l += A[i]
                i, j = i + 1, j - 1
            elif l > r:
                r += A[j]
                j -= 1
            else:
                l += A[i]
                i += 1
            if l != r:
                res += 1
        return res