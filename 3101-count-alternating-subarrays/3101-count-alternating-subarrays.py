class Solution:
    def countAlternatingSubarrays(self, A: List[int]) -> int:
        res, count = 0, 0
        last = -1
        for num in A:
            if last != num:
                count += 1
            else:
                count = 1
            last = num
            res += count
        return res