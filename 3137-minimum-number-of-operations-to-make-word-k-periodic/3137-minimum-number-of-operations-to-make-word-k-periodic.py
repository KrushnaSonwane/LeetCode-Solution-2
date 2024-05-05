class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        A = Counter()
        B = []
        for i in range(len(word)):
            if i % k == 0:
                A[''.join(B)] += 1
                B = []
            B.append(word[i])
        A[''.join(B)] += 1
        return len(word) // k - max(A.values())