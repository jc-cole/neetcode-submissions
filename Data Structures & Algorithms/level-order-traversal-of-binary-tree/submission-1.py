# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    traversalList = None
    def levelOrder(self, root: Optional[TreeNode], depth=0, first=True) -> List[List[int]]:
        if first:
            self.traversalList = None
        if not root:
            if self.traversalList == None:
                self.traversalList = []
        else:
            self.levelOrder(root.left, depth=depth+1, first=False)
            self.levelOrder(root.right, depth=depth+1, first=False)
            while len(self.traversalList) <= depth:
                self.traversalList.append([])
            self.traversalList[depth].append(root.val)
        return self.traversalList