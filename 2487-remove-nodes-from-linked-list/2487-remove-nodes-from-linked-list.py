# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def revNode(head):
            nxt, prev = None, None
            res = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev
        head = revNode(head)
        t = head
        while t and t.next:
            if t.val <= t.next.val:
                t = t.next
            else:
                t.next = t.next.next
        return revNode(head)