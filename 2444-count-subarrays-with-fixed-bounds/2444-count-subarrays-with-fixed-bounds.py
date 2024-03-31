class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        queue = deque()
        for i, num in enumerate(nums):
            if num >= minK and num <= maxK:
                queue.append(num)
            if num < minK or num > maxK or i == len(nums) - 1:
                f, s = -1, -1
                for i, num in enumerate(queue):
                    if num == minK:
                        f = i
                    if num == maxK:
                        s = i
                    res += min(f, s) + 1
                queue = []
        return res