# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head.next: return None
        p1, p2 = head, head
        for _ in range(n):
            p1 = p1.next
        while p1 and p1.next:
            p2 = p2.next
            p1 = p1.next
        if p1 is None: return head.next
        p2.next = p2.next.next
        return head