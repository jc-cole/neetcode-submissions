# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root = TreeNode(val=preorder[0])
        if len(preorder) == 1:
            return root

        rootIdx = inorder.index(preorder[0])
        leftInOrder, leftSet = inorder[:rootIdx], set(inorder[:rootIdx])
        rightInOrder, rightSet = inorder[rootIdx+1:], set(inorder[rootIdx+1:])
        leftPreOrder = []
        rightPreOrder = []

        for num in preorder[1:]:
            if num in leftSet:
                leftPreOrder.append(num)
            elif num in rightSet:
                rightPreOrder.append(num)
            else:
                assert False
        
        root.left = self.buildTree(leftPreOrder, leftInOrder)
        root.right = self.buildTree(rightPreOrder, rightInOrder)
        
        return root
        
