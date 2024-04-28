class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        @cache
        def dfs(i, remove, diff, taken):
            # print(i, remove, diff, taken)
            if remove >= 3: return inf
            if taken == len(nums2): return diff
            if i == len(nums1): return diff
            res = dfs(i+1, remove + 1, diff, taken)
            if diff == inf:
                res = min(res, dfs(i+1, remove, nums2[i-remove] - nums1[i], taken+1))
            else:
                if diff == nums2[i-remove] - nums1[i]:
                    res = min(res, dfs(i+1, remove, diff, taken+1))
                else:
                    res = min(res, dfs(i+1, remove+1, diff, taken))
            return res
        return dfs(0, 0, inf, 0)