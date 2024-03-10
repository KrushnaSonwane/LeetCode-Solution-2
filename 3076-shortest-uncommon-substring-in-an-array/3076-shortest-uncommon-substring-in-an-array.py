class Solution:
    def shortestSubstrings(self, A: List[str]) -> List[str]:
        res = []
        for i in range(len(A)):
            hashT = set()
            for j in range(len(A)):
                if i == j: continue
                w = A[j]
                for x in range(len(w)):
                    for y in range(x+1, len(w)+1):
                        hashT.add(w[x:y])
            t = []
            w = A[i]
            for x in range(len(w)):
                for y in range(x+1, len(w)+1):
                    t.append(w[x:y])
            t.sort()
            res.append('a'*21)
            for num in t:
                if num not in hashT:
                    if len(res[-1]) > len(num):
                        res[-1] = num
                    elif len(res[-1]) == len(num):
                        res[-1] = min(num, res[-1])
            if res[-1] == 'a'*21:
                res[-1] = ''
        return res