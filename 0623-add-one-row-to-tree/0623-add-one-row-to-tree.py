# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            root = newNode
            return root
        idx = 1
        flag = False
        q = deque()
        q.append(root)
        while len(q):
            idx += 1
            for _ in range(len(q)):
                p = q.popleft()
                if idx == depth:
                    if p.left is not None:
                        newNode = TreeNode(val)
                        newNode.left = p.left
                        p.left = newNode
                    else:
                        newNode = TreeNode(val)
                        p.left = newNode
                        
                    if p.right is not None:
                        newNode = TreeNode(val)
                        newNode.right = p.right
                        p.right = newNode
                    else:
                        newNode = TreeNode(val)
                        p.right = newNode
                    flag = True
                else:
                    if p.left:
                        q.append(p.left)
                    if p.right:
                        q.append(p.right)
            if flag: break
        return root