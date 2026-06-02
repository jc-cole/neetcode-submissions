"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: return None
        correspondences = {
            None: None,
            head: Node(head.val)
        }
        old_curr = head
        new_curr = correspondences[head]
        while old_curr:
            if old_curr.next and not (old_curr.next in correspondences):
                correspondences[old_curr.next] = Node(old_curr.next.val)
            if old_curr.random and not (old_curr.random in correspondences):
                correspondences[old_curr.random] = Node(old_curr.random.val)

            new_curr.next = correspondences[old_curr.next]
            new_curr.random = correspondences[old_curr.random]

            old_curr = old_curr.next
            new_curr = new_curr.next
        
        return correspondences[head]
        

