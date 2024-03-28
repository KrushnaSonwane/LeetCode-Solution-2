from sortedcontainers import SortedList
class Solution:
    def numTeams(self, nums: List[int]) -> int:
        right, left = [0 for _ in nums], [0 for _ in nums]
        A, n = SortedList([nums[-1]]), len(nums)
        for i in range(n-2, -1, -1):
            right[i] = len(A) - bisect_right(A, nums[i])
            A.add(nums[i])
        A, res = SortedList([nums[0]]), 0
        for i in range(1, n):
            left[i] = len(A) - bisect_right(A, nums[i])
            A.add(nums[i])
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    res += right[j]
        for i in range(n-1, -1, -1):
            for j in range(i-1, -1, -1):
                if nums[i] < nums[j]:
                    res += left[j]
        return res