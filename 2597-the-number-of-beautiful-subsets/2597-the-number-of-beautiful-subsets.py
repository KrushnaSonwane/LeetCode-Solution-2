class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.res = 0
        def dfs(index, curr, n):
            if index == n:
                if len(curr) >= 1:
                    self.res += 1
                return
            if nums[index] - k not in curr and nums[index] + k not in curr:
                curr.append(nums[index])
                dfs(index + 1, curr, n)
                curr.pop()
            dfs(index + 1, curr, n)
        dfs(0, [], len(nums))
        return self.res