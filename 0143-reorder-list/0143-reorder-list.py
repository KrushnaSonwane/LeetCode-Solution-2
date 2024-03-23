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
        value = []
        node = head
        
        while node:
            value.append(node.val)
            node = node.next
        
        left = 0
        right = len(value) - 1
        
        node = head
        i = 0
        
        while node:
            if i % 2 == 0:
                node.val = value[left]
                left += 1
            else:
                node.val = value[right]
                right -= 1
            i += 1
            node = node.next
            
        return head