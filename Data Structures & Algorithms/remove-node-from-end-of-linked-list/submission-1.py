# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        
        prev, curr = None, head
        for _ in range(size - n):
            next = curr.next
            prev = curr
            curr = next
        
        if prev == None:
            return curr.next
    
        prev.next = curr.next
        return head