# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    blockedDepth = -1
    view = []
    def rightSideView(self, root: Optional[TreeNode], depth=0, first=True) -> List[int]:
        if not root:
            return []
        if first:
            self.blockedDepth = -1
            self.view = []
        if depth > self.blockedDepth:
            self.view.append(root.val)
            self.blockedDepth += 1
        self.rightSideView(root.right, depth=depth+1, first=False)
        self.rightSideView(root.left, depth=depth+1, first=False)
        return self.view

        