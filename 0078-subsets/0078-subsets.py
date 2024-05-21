class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, A):
            if i == len(nums):
                res.append([num for num in A])
                return 
            dfs(i+1, A)
            A.append(nums[i])
            B = [num for num in A]
            dfs(i+1, B.copy())
            A.pop()
        dfs(0, [])
        return res
            