# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, maxVal=None) -> int:
        if maxVal == None:
            maxVal = float("-inf")
        if not root:
            return 0
        
        isGood = root.val >= maxVal
        
        return int(isGood) + (
            self.goodNodes(root.left, maxVal=max(root.val, maxVal)) +
            self.goodNodes(root.right, maxVal=max(root.val, maxVal))
        )
        