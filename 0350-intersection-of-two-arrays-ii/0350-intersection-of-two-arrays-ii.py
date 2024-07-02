class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashT = collections.Counter(nums1)
        res = []
        for num in nums2:
            if num in hashT and hashT[num]:
                res.append(num)
                hashT[num] -= 1
        return res