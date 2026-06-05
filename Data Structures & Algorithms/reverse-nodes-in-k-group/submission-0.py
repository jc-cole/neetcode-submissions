# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseSublist(self, head):
        new_tail = head
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        new_head = prev
        return [new_head, new_tail]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy_head = ListNode()
        dummy_head.next = head
        prev_group_tail = dummy_head

        while prev_group_tail.next:
            sublist_head = prev_group_tail.next
            curr = prev_group_tail.next
            ct = 0

            while curr.next and ct < (k - 1):
                ct += 1
                curr = curr.next
            
            if (not curr.next) and ct < (k - 1):
                return dummy_head.next

            next_group_head = curr.next
            curr.next = None
            new_head, new_tail = self.reverseSublist(sublist_head)
            prev_group_tail.next = new_head
            prev_group_tail = new_tail
            prev_group_tail.next = next_group_head
        
        return dummy_head.next
        
        