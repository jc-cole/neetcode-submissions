class Solution:
    def potentialSubroots(self, root, subRoot, matching=None): 
        if matching is None:
            matching = []
        if not root:
            return matching
        if root.val == subRoot.val:
            matching.append(root)
        self.potentialSubroots(root.left, subRoot, matching=matching)
        self.potentialSubroots(root.right, subRoot, matching=matching)
        return matching
    
    def isEquivalentTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            return (
                self.isEquivalentTree(root.left, subRoot.left) and
                self.isEquivalentTree(root.right, subRoot.right)
            )
        else:
            return False

        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        toCheck = self.potentialSubroots(root, subRoot, matching=None)
        return any(
            self.isEquivalentTree(matchingRoot, subRoot)
            for matchingRoot in toCheck
        )