# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # [absMax, maxRootPath]
        def search(node):
            if node == None:
                return [float("-inf"), float("-inf")]
            absMaxLeft, pathMaxLeft = search(node.left)
            absMaxRight, pathMaxRight = search(node.right)

            maxRootPivot = pathMaxRight + pathMaxLeft + node.val
            maxRootPath = max([pathMaxRight, pathMaxLeft, 0]) + node.val
            absMax = max([absMaxLeft, absMaxRight, maxRootPath, maxRootPivot])

            return [absMax, maxRootPath]
        
        maxSum, _ = search(root)

        return maxSum
        