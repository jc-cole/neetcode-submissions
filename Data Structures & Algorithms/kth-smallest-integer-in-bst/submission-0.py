# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    nodesRemaining = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int, first=True) -> int:
        if first:
            self.nodesRemaining = k
        if not root:
            return -1
        leftTraversal = self.kthSmallest(root.left, k, first=False)
        if leftTraversal >= 0:
            return leftTraversal
        self.nodesRemaining -= 1
        if self.nodesRemaining == 0:
            return root.val
        return self.kthSmallest(root.right, k, first=False)
