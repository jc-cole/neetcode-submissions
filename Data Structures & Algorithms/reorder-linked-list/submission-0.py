# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        reversed_half = self.reverseList(mid.next)
        mid.next = None

        while reversed_half:
            next = head.next
            head.next = reversed_half
            rev_next = reversed_half.next
            reversed_half.next = next
            head = next
            reversed_half = rev_next


        
