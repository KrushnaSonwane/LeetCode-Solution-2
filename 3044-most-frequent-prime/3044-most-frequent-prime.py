class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def is_prime(n):
            if n == 1:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        A = Counter()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                a, b = i, j
                for x, y in [(1, 0), (-1,0), (1,-1), (-1,1), (0,1), (0,-1), (1,1), (-1,-1)]:
                    a, b = i, j
                    num = ''
                    while 0 <= a < len(mat) and 0 <= b < len(mat[0]):
                        num += str(mat[a][b])
                        A[num] += 1
                        a += x
                        b += y
        count, res = 0, -1
        for num in A:
            if int(num) > 10 and is_prime(int(num)):
                if A[num] > count:
                    count, res = A[num], int(num)
                elif A[num] == count:
                    res = max(res, int(num))
        return res