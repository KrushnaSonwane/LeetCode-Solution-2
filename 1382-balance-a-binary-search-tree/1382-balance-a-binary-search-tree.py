# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root: return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        arr = []
        dfs(root)
        def solve(l, r):
            if l > r: return None
            mid = (l + r) // 2
            root = TreeNode(arr[mid])
            root.left = solve(l, mid - 1)
            root.right = solve(mid + 1, r)
            return root
        return solve(0, len(arr) - 1)