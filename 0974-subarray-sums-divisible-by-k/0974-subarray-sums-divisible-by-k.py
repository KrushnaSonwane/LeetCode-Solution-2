class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count, sum_, hashT = 0, 0, {0: 1}
        for num in nums:
            sum_ += num
            mod = sum_ % k
            if mod in hashT:
                count += hashT[mod]
                hashT[mod] += 1
            else:
                hashT[mod] = 1
        return count