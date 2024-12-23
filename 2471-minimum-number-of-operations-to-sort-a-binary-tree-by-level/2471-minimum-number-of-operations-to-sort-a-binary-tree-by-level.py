# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swap(arr, n):

            r = 0
            temp = []
            for i in arr: temp.append(i)

            hashT = {}

            temp.sort()

            for i in range(n):
                hashT[arr[i]] = i

            init = 0

            for i in range(n):
                if (arr[i] != temp[i]):
                    r += 1
                    init = arr[i]
                    arr[i], arr[hashT[temp[i]]] = arr[hashT[temp[i]]], arr[i]
                    hashT[init] = hashT[temp[i]]
                    hashT[temp[i]] = i
            return r
        q = deque()
        q.append(root)
        ans = 0
        while q:
            t = []
            count = 0
            for _ in range(len(q)):
                p = q.popleft()
                t.append(p.val)
                if p.left: q.append(p.left)
                if p.right: q.append(p.right)
            c = swap(t, len(t))
            ans += c
        return ans