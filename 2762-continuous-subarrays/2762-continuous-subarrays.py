from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, A: List[int]) -> int:
        min_, max_ = SortedList(), SortedList()
        j = 0
        res = 0
        for i, num in enumerate(A):
            min_.add([num, i])
            while abs(num-min_[0][0]) > 2 or abs(num-min_[-1][0]) > 2:
                min_.discard([A[j], j])
                j += 1
            res += len(min_)
        return res