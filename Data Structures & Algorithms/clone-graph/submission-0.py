"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        oldToCopy = {}
        copyStart = Node(val = node.val)
        oldToCopy[node] = copyStart
        def dfs(old, copy):
            for neighbor in old.neighbors:
                if neighbor in oldToCopy:
                    copy.neighbors.append(oldToCopy[neighbor])
                else:
                    new = Node(val=neighbor.val)
                    oldToCopy[neighbor] = new
                    dfs(neighbor, new)
                    copy.neighbors.append(new)
        dfs(node, copyStart)
        return copyStart
