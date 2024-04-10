class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        A = [i for i in range(len(deck))]
        res = [_ for _ in deck]
        for num in sorted(deck):
            i = A.pop(0)
            res[i] = num
            if A:
                A.append(A.pop(0))
        return res