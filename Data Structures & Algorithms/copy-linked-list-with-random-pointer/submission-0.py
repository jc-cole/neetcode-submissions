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
            str(None): None,
            str(head): Node(head.val)
        }
        old_curr = head
        new_curr = correspondences[str(head)]
        while old_curr:
            if old_curr.next and not (str(old_curr.next) in correspondences):
                correspondences[str(old_curr.next)] = Node(old_curr.next.val)
            if old_curr.random and not (str(old_curr.random) in correspondences):
                correspondences[str(old_curr.random)] = Node(old_curr.random.val)

            new_curr.next = correspondences[str(old_curr.next)]
            new_curr.random = correspondences[str(old_curr.random)]

            old_curr = old_curr.next
            new_curr = new_curr.next
        
        return correspondences[str(head)]
        

