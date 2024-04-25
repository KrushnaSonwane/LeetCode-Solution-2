class Solution:
    def maxTrailingZeros(self, A: List[List[int]]) -> int:
        @cache
        def getCount(num):
            a, b = 0, 0
            while num%2==0:
                a += 1
                num //= 2
            while num%5==0:
                b+=1
                num//=5
            return [a, b]

        left, res = [], 0
        for i in range(len(A)):
            a, b, t = 0, 0, []
            for j in range(len(A[0])):
                t.append([a, b])
                a += getCount(A[i][j])[0]
                b += getCount(A[i][j])[1]
            left.append(t)

        right = []
        for i in range(len(A)):
            a, b, t = 0, 0, []
            for j in range(len(A[0])-1, -1, -1):
                t.append([a, b])
                a += getCount(A[i][j])[0]
                b += getCount(A[i][j])[1]
            right.append(t[::-1])

        top, bottom = [[0 for _ in A[0]] for _ in A], [[0 for _ in A[0]] for _ in A]
        for j in range(len(A[0])):
            a, b = 0, 0
            for i in range(len(A)):
                top[i][j] = [a, b]
                a += getCount(A[i][j])[0]
                b += getCount(A[i][j])[1]

        for j in range(len(A[0])):
            a, b = 0, 0
            for i in range(len(A)-1, -1, -1):
                bottom[i][j] = [a, b]
                a += getCount(A[i][j])[0]
                b += getCount(A[i][j])[1]

        for i in range(len(A)):
            for j in range(len(A[i])):
                for xx, yy in [top[i][j], bottom[i][j]]:
                    for x, y in [left[i][j], right[i][j]]:
                        x += getCount(A[i][j])[0]
                        y += getCount(A[i][j])[1]
                        res = max(res, min(xx+x, yy+y))
                        
        return res