# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = [-1, 0]
        def dfs(root, size):
            if not root: return 
            if self.res[0] < size:
                self.res[1] = root.val
                self.res[0] = size
            dfs(root.left, size+1)
            dfs(root.right, size+1)
        dfs(root, 0)
        return self.res[1]
