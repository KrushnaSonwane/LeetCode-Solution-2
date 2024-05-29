class Solution:
    def numSteps(self, s: str) -> int:
        A, res = [ch for ch in s], 0
        while len(A) > 1:
            if A[-1] == '1':
                i = len(A)-1
                while i >= 0 and A[i] == '1':
                    i -= 1
                if i == -1:
                    A = ['1'] + ['0' for _ in A]
                else:
                    A[i] = '1'
                    i += 1
                    while i < len(A):
                        A[i] = '0'
                        i += 1
            else:
                A.pop()
            res += 1
        return res