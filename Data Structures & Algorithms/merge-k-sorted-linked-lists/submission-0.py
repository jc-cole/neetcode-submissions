# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        
        while any(lists):
            min_idx = min(
                [idx for idx in range(len(lists)) if lists[idx]], 
                key = lambda idx : lists[idx].val
            )

            curr.next = lists[min_idx]
            curr = curr.next
            lists[min_idx] = lists[min_idx].next
        
        return head.next

        