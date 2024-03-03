class Solution:
    def resultArray(self, N: List[int]) -> List[int]:
        A, B = [N[0]], [N[1]]
        for num in N[2:]:
            if A[-1] > B[-1]:
                A.append(num)
            else:
                B.append(num)
        return A + B