# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        new = slow.next
        slow.next = None
        prev, node = None, None
        while new:
            nxt = new.next
            new.next = prev
            prev = new
            new = nxt
        res = head
        while res and prev:
            nxt1 = res.next
            nxt2 = prev.next
            prev.next = None
            res.next = prev
            res.next.next = nxt1
            prev = nxt2
            res = res.next.next
        return head