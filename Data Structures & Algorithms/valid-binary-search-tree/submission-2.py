# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], max=None, min=None) -> bool:
        if max == None and min == None:
            max = float("inf")
            min = float("-inf")
            
        
        if root == None:
            return True
        
        if not (min < root.val < max):
            return False
            
        left = self.isValidBST(root.left, max=root.val, min=min)
        right = self.isValidBST(root.right, max=max, min=root.val)

        return left and right

        
                
    

