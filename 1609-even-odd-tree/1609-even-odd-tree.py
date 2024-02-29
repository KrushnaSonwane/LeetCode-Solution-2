# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        Q, even = [root], False
        while Q:
            even = not even
            last = inf if not even else -inf
            for _ in range(len(Q)):
                root = Q.pop(0)
                if even and (last >= root.val or root.val%2 == 0):
                    return False
                if not even and (root.val >= last or root.val%2):
                    return False
                last = root.val
                for child in [root.left, root.right]:
                    if child: Q.append(child)
        return True