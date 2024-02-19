class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        if k == 1: return '4'
        if k == 2: return '7'
        sum_, A = 2, ['']
        while k-1 >= sum_:
            k -= sum_
            sum_ += sum_
            A.append('')
        i, k = len(A)-1, k-1
        while i >= 0:
            A[i] = '7' if k and k % 2 else '4'
            k //= 2
            i -= 1
        return ''.join(A)