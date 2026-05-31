# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None, new_head=None) -> Optional[ListNode]:
        if head == None:
            return prev
        else:
            to_reverse = head.next
            head.next = prev
            return self.reverseList(to_reverse, prev=head)
            

