class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList
        queue = SortedList()
        n, res, ptr = len(nums), 0, 0
        for i, num in enumerate(nums):
            queue.add([num, i])
            while queue and n > ptr and queue[-1][0] - queue[0][0] > limit:
                queue.discard([nums[ptr], ptr])
                ptr += 1
            res = max(res, len(queue))
        return res