class Solution:
    def minimumSubarrayLength(self, A: List[int], k: int) -> int:
        res = inf
        count = Counter()
        j, sum_ = 0, 0
        for i in range(len(A)):
            if A[i] >= k: return 1
            sum_ |= A[i]
            jj = 0
            a = A[i]
            while a:
                count[jj] += a % 2
                a //= 2
                jj += 1
            while j <= i and sum_ >= k:
                jj = 0
                a = A[j]
                while a:
                    t = a % 2 
                    count[jj] -= int(a % 2 and a % 2 == 1)
                    a //= 2
                    if count[jj] == 0 and t:
                        sum_ -= 2 ** jj
                    jj += 1
                res = min(res, i - j + 1)
                j += 1
        return max(1, res) if res != inf else -1