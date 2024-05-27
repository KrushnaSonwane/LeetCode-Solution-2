class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        hashT = []
        for i, num in enumerate(nums):
            if num == x:
                hashT.append(i)
        res = []
        for num in queries:
            if len(hashT) < num:
                res.append(-1)
            else:
                res.append(hashT[num-1])
        return res