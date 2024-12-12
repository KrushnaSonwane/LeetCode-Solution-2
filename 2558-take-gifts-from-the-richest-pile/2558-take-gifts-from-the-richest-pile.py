import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        queue = [-num for num in gifts]
        heapq.heapify(queue)
        sum_ = sum(gifts)
        while k:
            p = -heapq.heappop(queue)
            sum_ -= p
            root = math.isqrt(p)
            sum_ += root
            heapq.heappush(queue, -root)
            k -= 1
        return sum_