class Solution:
    def minimumAddedInteger(self, A: List[int], B: List[int]) -> int:
        A.sort()
        B.sort()
        C, count = set(), Counter()
        for i in range(3):
            C.add(B[0]-A[i])
        
        for key in C:
            i, j = 0, 0
            while i < len(A) and j < len(B):
                while i < len(A) and B[j]-A[i] != key:
                    i += 1
                if i < len(A) and B[j]-A[i] == key:
                    count[key] += 1
                i += 1
                j += 1  
        res = inf
        for key in C:
            if count[key] >= len(B):
                res = min(res, key)
        return res