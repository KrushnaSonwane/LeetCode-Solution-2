class Solution:
    def unmarkedSumArray(self, A: List[int], Q: List[List[int]]) -> List[int]:
        sum_ = sum(A)
        marked = set()
        AA = sorted([[num, i] for i, num in enumerate(A)])
        res = []
        for i, k in Q:
            if i not in marked:
                sum_ -= A[i]
                marked.add(i)
            while k and AA:
                num, j = AA.pop(0)
                if j in marked: continue
                sum_ -= num
                marked.add(j)
                k -= 1
            res.append(sum_)
        return res