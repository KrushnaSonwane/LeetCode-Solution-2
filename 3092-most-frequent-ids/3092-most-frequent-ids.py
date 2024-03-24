from sortedcontainers import SortedList
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        A = SortedList()
        hashT = {}
        res = []
        for num, count in zip(nums, freq):
            if num in hashT:
                A.discard(hashT[num])
                hashT[num] += count
            else:
                hashT[num] = count
            A.add(hashT[num])
            res.append(max(0, A[-1]))
        return res