class Solution:
    def decodeCiphertext(self, S: str, rows: int) -> str:
        A, i = [], 0
        for _ in range(rows):
            t = []
            for _ in range(len(S)//rows):
                t.append(S[i])
                i += 1
            A.append(t)
        res, x = [], 0
        for _ in range(len(S)//rows):
            i, j = 0, x
            for _ in range(rows):
                if j < len(S) // rows:
                    res.append(A[i][j])
                i += 1
                j += 1
            x += 1
        while res and res[-1] == ' ':
            res.pop()
        return ''.join(res)