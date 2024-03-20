# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        aa, bb = list1, list1
        for _ in range(b+1):
            bb = bb.next
        for _ in range(a-1):
            aa = aa.next
        t = list2
        while t.next:
            t = t.next
        aa.next = list2
        t.next = bb
        return list1