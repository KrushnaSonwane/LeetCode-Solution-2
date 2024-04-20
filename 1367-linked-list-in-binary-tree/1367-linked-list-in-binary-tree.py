# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @cache
        def dfs(root, head, start):
            if not head: return True
            if not root: return False
            res = False
            if not start:
                res = dfs(root.left, head, False) or dfs(root.right, head, False)
            if head.val == root.val:
                res = res or dfs(root.right, head.next, True) or dfs(root.left, head.next, True)
            return res
        return dfs(root, head, False)