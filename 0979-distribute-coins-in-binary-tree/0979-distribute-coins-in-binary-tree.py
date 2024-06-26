# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            res[0] += abs(l) + abs(r)
            return l + r + (root.val - 1)
        dfs(root)
        return res[0]