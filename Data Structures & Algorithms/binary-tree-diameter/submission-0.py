# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depths = defaultdict(int)
    def depth(self, root=None):
        if not root:
            return 0
        my_depth = max(self.depth(root.left), self.depth(root.right)) + 1
        self.depths[root] = my_depth
        return my_depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode], first=True) -> int:
        # circumference of arbitrary node is:
        # 0 if no left or right children (base case) or
        # the largest out of
        # 1. The circumference of the left child
        # 2. The circumference of the right child
        # 3. The depth(left) + depth(right)
        if first:
            self.depth(root=root)

        if not (root and root.left) and  not (root and root.right):
            return 0
        else:
            left_diameter = self.diameterOfBinaryTree(root.left, first=False)
            right_diameter = self.diameterOfBinaryTree(root.right, first=False)
            diameter_through_root = self.depths[root.left] + self.depths[root.right]
            return max([
                left_diameter,
                right_diameter,
                diameter_through_root
            ])
        
