# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root, s):
            if not root: return s
            if not root.left and not root.right: return chr(root.val+97)+s
            res = ''
            if root.left:
                res = dfs(root.left, chr(root.val+97)+s)
            if root.right:
                ans = dfs(root.right, chr(root.val+97)+s)
                if not res: res = ans
                else: res = min(res, ans)
            return res
        return dfs(root, '')