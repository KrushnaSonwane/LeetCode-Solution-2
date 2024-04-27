class Solution:
    def canMakeSquare(self, B: List[List[str]]) -> bool:
        A = Counter()
        A[B[0][0]] += 1
        A[B[0][1]] += 1
        A[B[1][1]] += 1
        A[B[1][0]] += 1
        for key in A.values():
            # if key == 1: return True
            if key == 1 or key == 4: return True
        A = Counter()
        A[B[0][2]] += 1
        A[B[0][1]] += 1
        A[B[1][1]] += 1
        A[B[1][2]] += 1
        for key in A.values():
            # if key == 1: return True
            if key == 1 or key == 4: return True
        A = Counter()
        A[B[2][0]] += 1
        A[B[2][1]] += 1
        A[B[1][1]] += 1
        A[B[1][0]] += 1
        for key in A.values():
            # if key == 1: return True
            if key == 1 or key == 4: return True
        A = Counter()
        A[B[2][2]] += 1
        A[B[2][1]] += 1
        A[B[1][1]] += 1
        A[B[1][2]] += 1
        for key in A.values():
            if key == 1 or key == 4: return True
        return False
        
        