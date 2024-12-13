class Solution:
    def findScore(self, nums: List[int]) -> int:
        queue = [[val, i] for i, val in enumerate(nums)]
        heapq.heapify(queue)
        res = 0
        marked = set()
        while queue:
            val, index = heapq.heappop(queue)
            if index not in marked:
                marked.add(index)
                marked.add(index - 1)
                marked.add(index + 1)
                res += val
        return res