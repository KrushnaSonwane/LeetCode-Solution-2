class Solution:
    def maximumCoins(self, H: List[int], M: List[int], C: List[int]) -> List[int]:
        M = sorted([[M[i], C[i]] for i in range(len(M))])
        sum_, res, j = 0, [0 for _ in H], 0
        H = sorted([[H[i], i] for i in range(len(H))])
        for power, i in H:
            while j < len(M) and power >= M[j][0]:
                sum_ += M[j][1]
                j += 1
            res[i] = sum_
        return res