class Solution:
    def bagOfTokensScore(self, A: List[int], p: int) -> int:
        A.sort()
        res, score = 0, 0
        l, r = 0, len(A)-1
        while r >= l:
            if p >= A[l]:
                score += 1
                p -= A[l]
                l += 1
            elif score >= 1:
                score -= 1
                p += A[r]
                r -= 1
            else: 
                break
            res = max(res, score)
        return res