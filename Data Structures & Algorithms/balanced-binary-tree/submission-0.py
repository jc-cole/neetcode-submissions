# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depths = defaultdict(int)
    def depth(self, root):
        if not root:
            return 0
        my_depth = max(self.depth(root.left), self.depth(root.right)) + 1
        self.depths[root] = my_depth
        return my_depth

    def isBalanced(self, root: Optional[TreeNode], first=True) -> bool:

        if not root:
            return True

        if first:
            self.depth(root)

        if abs(self.depths[root.left] - self.depths[root.right]) <= 1:
            return self.isBalanced(root.left, first=False) and self.isBalanced(root.right, first=False)
        else:
            return False
                
        